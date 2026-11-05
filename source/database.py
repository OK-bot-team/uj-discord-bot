import sqlite3
import discord
import asyncio
import time


async def sendReminder(bot, remID, userID, channelID, messageID):
    with sqlite3.connect('data/okbot.db') as database:
        cursor = database.cursor()
        _ = cursor.execute("DELETE FROM reminders WHERE id = ?", (remID,))

    try:
        channel = bot.get_channel(channelID) or await bot.fetch_channel(channelID)
        try:
            await channel.get_partial_message(messageID)\
                         .reply(f"It's time bro <@{userID}>!")
        except discord.HTTPException:
            await channel.send(f"It's time bro <@{userID}>!")
    except Exception:
        pass

    try:
        if user := bot.get_user(userID) or await bot.fetch_user(userID):
            await user.send('Its time bro!')
    except Exception:
        pass


def getNextReminder():
    result = ()

    with sqlite3.connect('data/okbot.db') as database:
        cursor = database.cursor()
        cursor.execute("""
            SELECT id, userID, channelID, messageID, date 
            FROM reminders 
            ORDER BY date ASC LIMIT 1
        """)

        result = cursor.fetchone()

    return result


async def reminderRoutine(bot):
    await bot.wait_until_ready()
    
    while True:
        try:
            bot.newReminder.clear()

            if reminder := getNextReminder():
                remID, userID, channelID, messageID, date = reminder
                now = time.time()

                if date <= now:
                    await sendReminder(bot, remID, userID, channelID, messageID)
                else: 
                    try:
                        await asyncio.wait_for(
                            bot.newReminder.wait(),
                            timeout = date - now
                        )
                    except asyncio.TimeoutError:
                        await sendReminder(bot, remID, userID, channelID, messageID)
            else:
                await bot.newReminder.wait()

        except Exception as e:
            print(f"[Reminder Error] Coś się popsuło: {e}", flush=True)


def init_database():
    import os
    os.makedirs("data", exist_ok=True)

    with sqlite3.connect('data/okbot.db') as database:
        _ = database.cursor().execute("""
            CREATE TABLE IF NOT EXISTS Reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userID INTEGER,
                channelID INTEGER,
                messageID INTEGER,
                date REAL
            )
        """)
