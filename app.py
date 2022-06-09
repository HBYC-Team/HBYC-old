"""
***************HBYC Bot*************
**********Author:hugocoding*********
********Release Date:2022.6.8*******
************Version:0.0.1***********
********License: BSD-3 Claude*******
****Develop OS: Ubuntu 20.04 LTS****
************************************
"""
import discord
from discord.ext import commands
from discord.commands import slash_command, Option

import json, os

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Bot(command_prefix=">", intents=intents)


@client.event
async def on_ready():
    print("Bot Logined")
    print(client.user)
    print("------------------------")

@client.slash_command(name = "load", description = "Load the Cog_Extension")
async def load(
    ctx,
    extension: Option(str, "Enter Extension Name")
):
    client.load_extension(f"cmds.{extension}")
    await ctx.respond(f"加載Cog: {extension} 完成!")

@client.slash_command(name = "unload", description = "Un-Load the Cog_Extension")
async def unload(
    ctx,
    extension: Option(str, "Enter Extension Name")
):
    client.unload_extension(f"cmds.{extension}")
    await ctx.respond(f"關閉Cog: {extension} 完成!")

@client.slash_command(name = "reload", description = "Re-Load the Cog_Extension")
async def reload(
    ctx,
    extension: Option(str, "Enter Extension Name")
):
    client.reload_extension(f"cmds.{extension}")
    await ctx.respond(f"重新加載Cog: {extension} 完成!")



with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        client.load_extension(f"cmds.{filename[:-3]}")



load_dotenv()
token = os.getenv("DISCORD_TOKEN")



if __name__ == "__main__":
    client.run(token)
    