from discord.ext import commands
from core.classes import Cog_Extension

import json

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("大佬"):
            await msg.channel.send("肯定是在說AC0xRPFS001#5007")

        if msg.content.startswith("?java"):
            await msg.channel.send("Java嗎？我不喜歡Java！！")



def setup(client):
    client.add_cog(Event(client))
