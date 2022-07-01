from discord.ext import commands
from core.classes import Cog_Extension

import json, random, time

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("大佬"):
            await msg.channel.send("肯定是在說<@!475958550699442176>")
            print("Event:大佬")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by:", msg.author)
            print("------")
        
        if msg.content.startswith("?java"):
            await msg.channel.send("Java嗎？我不喜歡Java！！")
            print("Event:Java")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by:", msg.author)
            print("------")
        
        if str(self.client.user.id) in msg.content and msg.author != self.client.user:
            got_mention = random.choice(conf["got_mention"])
            await msg.channel.send(f"{msg.author.mention} {got_mention}")
            print("Got Tag")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by:", msg.author)
            print("------")
        
        if str("爛bot") in msg.content and msg.author != self.client.user:
            await msg.channel.send(random.choice(conf["lanbot"]))
            print("Event:爛bot")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by:", msg.author)
            print("------")

        if msg.content == "/hekp" and msg.author != self.client.user:
            await msg.channel.send("尋求協助前先確認一下自己的單字有沒有拼錯吧")
            print("Event:hekp")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by", msg.author)
            print("------")

        if msg.content == "/he;p" and msg.author != self.client.user:
            await msg.channel.send("尋求協助前請先會拼這個單字")
            print("Event:hekp")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by", msg.author)
            print("------")

        if msg.content == "/heop" and msg.author != self.client.user:
            await msg.channel.send("尋求協助前請重修小學三年級英文")
            print("Event:hekp")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by", msg.author)
            print("------")

        if msg.content == "/he.p" and msg.author != self.client.user:
            await msg.channel.send("尋求協助前先確認一下自己的單字有沒有拼錯吧")
            print("Event:hekp")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by", msg.author)
            print("------")

        if msg.content == "爛恐龍" and msg.author != self.client.user:
            await msg.chnnel.send("你才爛你全家都爛") 
            print("Event:爛恐龍")
            fromserver = msg.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("from", fromserver)
            print("at", timestamp)
            print("by", msg.author)
            print("------")

def setup(client):
    client.add_cog(Event(client))