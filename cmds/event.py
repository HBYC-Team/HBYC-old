from discord.ext import commands
from core.classes import Cog_Extension

import json, random

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("大佬"):
            await msg.channel.send("肯定是在說AC0xRPFS001#5007")
            print("Event:大佬")
            fromserver = msg.author.guild.name
            print("from", fromserver)
            print("by:", msg.author)
            print("------")
        
        if msg.content.startswith("?java"):
            await msg.channel.send("Java嗎？我不喜歡Java！！")
            print("Event:Java")
            fromserver = msg.author.guild.name
            print("from", fromserver)
            print("by:", msg.author)
            print("------")
        
        if str(self.client.user.id) in msg.content and msg.author != self.client.user:
            got_mention = random.choice(conf["got_mention"])
            await msg.channel.send(f"{msg.author.mention} {got_mention}")
            print("Got Tag")
            fromserver = msg.author.guild.name
            print("from", fromserver)
            print("by:", msg.author)
            print("------")
        
        if str("爛bot") in msg.content and msg.author != self.client.user:
            await msg.channel.send("肯定是在說隔壁棚的Junior Hizollo哈哈哈哈爛bot")
            print("Event:爛bot")
            fromserver = msg.author.guild.name
            print("from", fromserver)
            print("by:", msg.author)
            print("------")


def setup(client):
    client.add_cog(Event(client))
