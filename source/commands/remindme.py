import time
import sqlite3


async def remindme_util(ctx, amount, unit):
    time_offsets = {"s": 1, "m": 60, "h": 3600, "d": 86400, "M": 2592000}

    if unit not in time_offsets.keys():
        await ctx.send("Wrong unit type")
        return

    try:
        amount = int(amount)
        if amount > 0:
            date = time.time() + amount * time_offsets[unit]

            with sqlite3.connect('data/okbot.db') as database:
                _ = database.cursor().execute("""
                    INSERT INTO Reminders
                        (userID, channelID, messageID, date)
                    VALUES
                        (?, ?, ?, ?)
                """, (ctx.author.id, ctx.channel.id, ctx.message.id, date))

            await ctx.send("Started reminder")

            ctx.bot.newReminder.set()
    except ValueError:
        await ctx.send("Time must be an integer")
        return
