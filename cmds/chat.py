import discord
from random import choices
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
        await ctx.respond("done", delete_after=0)
        await ctx.send(訊息內容)
        fromserver = ctx.author.guild.name
        print("/say", 訊息內容)
        print("from", fromserver)
        print("by:", ctx.author)
        print("------")
    
    @slash_command(name="repeat", description="讓機器人重複一句你說的話")
    async def repeat(
        self, 
        ctx, 
        *, 
        訊息內容: Option(str, "輸入你要機器人重複的話")):
        await ctx.respond(訊息內容)
        fromserver = ctx.author.guild.name
        print("/repeat", 訊息內容)
        print("from", fromserver)
        print("by:", ctx.author)
        print("------"
                )
    @slash_command(name="thinking", description="thinking")
    async def thinking(self, ctx, 種類: Option(str, "選擇thinking表情類型", choices=["normal", "cat", "attano","thonk","superthonk","raythonk","rainbowhtonk","owothonk","thongk","smile1","smile2","rayteethonk","blue", "10","distrotion", "pistol"])):
        fromserver = ctx.author.guild.name
        print("/thinking", 種類)
        print("from", fromserver)
        print("by:", ctx.author)
        print("------")
        
        if 種類 == "normal":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:thinking:974621588257398784>")

        if 種類 == "cat":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:cathink:985794732926074900>")

        if 種類 == "attano":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:attanothink:984310669425930251>")
        
        if 種類 == "thonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:thonk:984310370363645962>")
        
        if 種類 == "superthonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:superthonk:984310368790781992>")

        if 種類 == "raythonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:raythonk:984310421072773170>")

        if 種類 == "rainbowhtonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:rainbowthonk:984310367276650546>")

        if 種類 == "owothonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:owothonk:984310416672960553>")

        if 種類 == "thongk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:thongk:984310425648779325>")

        if 種類 == "smile1":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:smilethonk:984310424155611206>")

        if 種類 == "smile2":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:w_:984310372091703296>")

        if 種類 == "rayteethonk":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:rayteethonk:984310422637281342>")

        if 種類 == "blue":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:bluethonk:984310412256358450>")

        if 種類 == "10":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:10thonk:984310410738028604>")

        if 種類 == "distrotion":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:distrotionthonk:984310414097657877>")

        if 種類 == "pistol":
            await ctx.respond("done", delete_after=0)
            await ctx.send("<:pisthonk:984310418455539742>")
            
def setup(client):
    client.add_cog(Chat(client))
