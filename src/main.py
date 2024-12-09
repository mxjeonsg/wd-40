import os
import sys
import json

import discord
from discord.ext import commands

import bot_commands
import multilang
import ownutils


def fetchBotProperties() -> any:
    with open("app.json") as app_json:
        data = json.load(app_json)
    return data

app = fetchBotProperties()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=app["AppBehaviours"]["CommandPrefix"], intents=intents)

@bot.event
async def on_ready() -> None:
    print("Bot started successfully!")

@bot.command()
async def ping(ctx) -> None:
    await bot_commands.ping(ctx)

@bot.command()
async def yes(ctx) -> None:
    await bot_commands.yes(ctx)

@bot.command()
async def randomint(ctx) -> None:
    await bot_commands.getRandomInteger(ctx)

@bot.command()
async def quit(ctx) -> None:
    if app["AppBehaviours"]["AllowQuit"]:
        await bot_commands.quitBot(ctx)
    else:
        await ctx.send()


def runBot() -> None:
    if app["AppBehaviours"]["DontRun"] == False:
        token: str = open(app["AppFiles"]["token"], "r").read()
        bot.run(token)


DEBUG: bool = False
def main(argv: list[str]) -> int:
    if DEBUG == True:
        print(f"App data: %s" %(app))
        print("-------------------------------------")
    
    strings: object = multilang.Multilang("strings.json")

    runBot()

main(sys.argv)