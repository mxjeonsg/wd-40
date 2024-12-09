import random

## This functions are gonna get wrapped by upper
## functions with the `bot.command()` decorator in
# the main file.
async def template(ctx) -> None:
    ## If you're gonna just send shit
    ## as a message, just do:
    ctx.send("Whatever shit to send")

async def ping(ctx) -> None:
    await ctx.send("Pong!")

async def yes(ctx) -> None:
    await ctx.send("no")

async def getRandomInteger(ctx) -> None:
    rand: int = random.randint(0, 200)
    await ctx.send(f"Random integer: %d" %(rand))