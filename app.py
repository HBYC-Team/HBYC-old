"""
***************HBYC Bot*************
**********Author:hugocoding*********
********Release Date:2022.6.13*******
************Version:0.0.2***********
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
    for guild in client.guilds:
        print(guild.id, guild.name)
    print("------------------------")
    await client.change_presence(activity=discord.Game(name="/help"))
    

@client.slash_command(name = "load", description = "Load the Cog_Extension")
async def load(
    ctx,
    extension: Option(str, "Enter Extension Name", choices=["chat", "event","music", "help", "user"]),
    password: Option(str, "passwd")
):
    PermessionDeniedFrom = (f"{ctx.author} at {ctx.author.guild.name}")
    if password == passwd :
        client.load_extension(f"cmds.{extension}")
        await ctx.respond(f"加載Cog: {extension} 完成!")
        print(f"Loaded {extension}")
    else:
        await ctx.respond("密碼錯誤，如錯誤超過3次將直接把你列入使用黑名單(ban)，未來將無法使用HBYC")
        print("###Someone tried to load the cog###", PermessionDeniedFrom)

@client.slash_command(name = "unload", description = "Un-Load the Cog_Extension")
async def unload(
    ctx,
    extension: Option(str, "Enter Extension Name", choices=["chat", "event","music", "help", "user"]),
    password: Option(str, "passwd")
):
    PermessionDeniedFrom = (f"{ctx.author} at {ctx.author.guild.name}")
    if password == passwd :
        client.unload_extension(f"cmds.{extension}")
        await ctx.respond(f"關閉Cog: {extension} 完成!")
        print(f"UnLoaded {extension}")
    else:
        await ctx.respond("密碼錯誤，如錯誤超過3次將直接把你列入使用黑名單(ban)，未來將無法使用HBYC")
        print("###Someone tried to unload the cog###", PermessionDeniedFrom)


@client.slash_command(name = "reload", description = "Re-Load the Cog_Extension")
async def reload(
    ctx,
    extension: Option(str, "Enter Extension Name", choices=["chat", "event","music", "help", "user"]),
    password: Option(str, "passwd")
):
    PermessionDeniedFrom = (f"{ctx.author} at {ctx.author.guild.name}")
    if password == passwd :
        client.reload_extension(f"cmds.{extension}")
        await ctx.respond(f"重新加載Cog: {extension} 完成!")
        print(f"ReLoaded {extension}")
    else:
        await ctx.respond("密碼錯誤，如錯誤超過3次將直接把你列入使用黑名單(ban)，未來將無法使用HBYC")
        print("###Someone tried to reload the cog###", PermessionDeniedFrom)



with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        client.load_extension(f"cmds.{filename[:-3]}")


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
passwd = os.getenv("password")


if __name__ == "__main__":
    client.run(token)
    
