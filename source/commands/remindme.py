import asyncio


async def remindme_util(ctx, amount, unit):
    time_offsets = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'M': 2592000}

    if unit not in time_offsets.keys():
        await ctx.send("Wrong unit type")
        return

    try:
        amount = int(amount)
        if amount > 0:
            amount = amount * time_offsets[unit]
            await ctx.send("Started reminder")
            await asyncio.sleep(amount)
            await ctx.reply(f"It's time bro {ctx.author.mention}!")
            await ctx.author.send("Its time bro!")
    except ValueError:
        await ctx.send("Time must be an integer")
        return
