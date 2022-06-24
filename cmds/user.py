import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from core.classes import Cog_Extension
import random, time, asyncio, json

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)



class User(Cog_Extension):
    @slash_command(name="avatar", description="取得一個使用者的頭像")
    async def avatar(self, ctx, *, member: Option(discord.Member, required=False)):
        if not member:
            member = ctx.author
        userAvatar = member.avatar.url
        await ctx.respond(f"{ctx.author.mention} 這是你要看的使用者頭像")
        await ctx.send(f"{member}的頭像:")
        await ctx.send(userAvatar)
        fromserver = ctx.author.guild.name
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("/avatar", member)
        print("from", fromserver)
        print("at", timestamp)
        print("by", ctx.author)
        print("------")
    
    @slash_command(name="report", description="將建議或錯誤回報給後台")
    async def report(self, ctx, 回報內容: Option(str, "請在這裡填入錯誤或建議內容，會回報到作者的後台")):
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

    @slash_command(name="ping", description="看看機器人的跑速")
    async def ping(self, ctx):
        await ctx.respond(f"🇵 🇴 🇳 🇬❗| 機器人延遲:{round(self.client.latency*1000)} (ms)")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("/ping")
        print(f"HBYC's ping:{round(self.client.latency*1000)}(ms)")
        print("from", ctx.author.guild.name)
        print("by", ctx.author)
        print("at", timestamp)
        print("-------")

    @slash_command(name="clean", description="清除一定數量的訊息")
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
        await ctx.respond("The message has been cleaned^__^")
        time.sleep(3)

    
    @slash_command(name="presence", description="更換目前機器人的動態")
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def presence(self, ctx):
        game = random.choice(conf["presence"])
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("/presence")
        print(f"Presence changed:{game}")
        print("from", ctx.author.guild.name)
        print(f"at {timestamp}")
        print("-------")
        await self.client.change_presence(activity=discord.Game(name=game))
        await ctx.respond(f"{ctx.author.mention}，已經將動態更改為`{game}`，5分鐘後可以再次使用這個指令！")


def setup(client):
    client.add_cog(User(client))
