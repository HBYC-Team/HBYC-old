######################################
#********HBYC Bot User Commands******#
#*********Author:dragonyc1002********#
#*******Release Date:2022.07.05******#
#************Version:0.0.5***********#
#********License: BSD 3-Clause*******#
#****Develop OS: Ubuntu 20.04 LTS****#
######################################
import discord
from discord.ext import commands, bridge
from discord.ext.bridge.core import BridgeOption
from core.classes import Cog_Extension
import random, time, asyncio, json

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)



class User(Cog_Extension):
    @bridge.bridge_command(name="avatar", description="取得一個使用者的頭像", aliases=["av"])
    async def avatar(self, ctx, 用戶: BridgeOption(discord.Member, required=False)):
        if not 用戶:
            member = ctx.author
        userAvatar = 用戶.avatar.url
        await ctx.respond(f"{ctx.author.mention} 這是你要看的使用者頭像\n {用戶}的頭像:")
        await ctx.send(userAvatar)
        print("/avatar", 用戶)
        print("from", ctx.author.guild.name)
        print("at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("by", ctx.author)
        print("------")
    

    @bridge.bridge_command(name="report", description="將建議或錯誤回報給後台", aliases=["rp"])
    async def report(self, ctx, 回報內容: BridgeOption(str, "請在這裡填入錯誤或建議內容，會回報到作者的後台")):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        embed=discord.Embed(title="**回報資訊**", color=0x4b56a8)
        embed.set_author(name=f"回報用戶：{ctx.author}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="使用者回報內容", value=f"`{回報內容}`", inline=False)
        embed.set_footer(text=f"你的回報內容已經送至後台 ‧ {timestamp}")
        await ctx.respond(embed=embed)
        print("######## User Report ########")
        print(f"***From Server {ctx.author.guild.name}***")
        print(f"***From User {ctx.author}***")
        print(回報內容)
        print("At", timestamp)
        print("#############################")
        print("-------")


    @bridge.bridge_command(name="ping", description="看看機器人的跑速")
    async def ping(self, ctx):
        await ctx.respond(f"🇵 🇴 🇳 🇬❗| 機器人延遲:{round(self.client.latency*1000)} (ms)")
        print("/ping")
        print(f"HBYC's ping:{round(self.client.latency*1000)}(ms)")
        print("from", ctx.author.guild.name)
        print("by", ctx.author)
        print("at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("-------")

    @bridge.bridge_command(name="clean", description="清除一定數量的訊息")
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, 刪除訊息數: int):
        await ctx.channel.purge(limit=刪除訊息數+1)
        await ctx.respond("The message has been cleaned^__^")
        time.sleep(3)

    
    @bridge.bridge_command(name="presence", description="更換目前機器人的動態", aliases=["ps"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def presence(self, ctx):
        game = random.choice(conf["presence"])
        print("/presence")
        print(f"Presence changed:{game}")
        print("from", ctx.author.guild.name)
        print(f"at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("-------")
        await self.client.change_presence(activity=discord.Game(name=game))
        await ctx.respond(f"{ctx.author.mention}，已經將動態更改為`{game}`，5分鐘後可以再次使用這個指令！")


    @bridge.bridge_command(name="announcement", description="機器人目前最新版本的內容", aliases=["an"])
    async def announcement(self, ctx):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        embed=discord.Embed(title="**HBYC的最新公告**", description=None, color=0x0080FF)
        embed.set_author(name="HBYC#1512", icon_url="https://i.imgur.com/cuu63j3.jpg")
        embed.add_field(name="**目前更新版本內容**", value="更新內容", inline=False)
        embed.add_field(name="🔵v0.0.4", value="發布日期:2022.07.01", inline=False)
        embed.add_field(name="🔴移除內容", value="無", inline=False)
        embed.add_field(name="🔴新增內容", value=">新增訊息指令，現在可以使用c![指令名稱]了!\n >新增部份隱藏反應", inline=True)
        embed.set_footer(icon_url=ctx.author.avatar.url, text=f"{ctx.author} ‧ {timestamp}")
        await ctx.respond(embed=embed)
        print("/announcement")
        print("from", ctx.author.guild.name)
        print(f"at {timestamp}")
        print("-------")

def setup(client):
    client.add_cog(User(client))
