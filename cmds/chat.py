from core.classes import Cog_Extension
from discord.commands import slash_command, Option
import json

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)

class Chat(Cog_Extension):
    @slash_command(name="say", description="讓機器人替你說一句話")
    async def say(
        self, 
        ctx, 
        *, 
        訊息內容: Option(str, "輸入你要機器人說的話")
    ):
        await ctx.send(訊息內容)
    
    @slash_command(name="repeat", description="讓機器人重複一句你說的話")
    async def repeat(
        self, 
        ctx, 
        *, 
        訊息內容: Option(str, "輸入你要機器人重複的話")):
        await ctx.respond(訊息內容)
    
    @slash_command(name="thinking", description="thinking")
    async def thinking(self, ctx):
        await ctx.send("<:thinking:974621588257398784>")

    
def setup(client):
    client.add_cog(Chat(client))