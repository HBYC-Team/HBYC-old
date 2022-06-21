import discord


from discord.commands import slash_command, Option
from core.classes import Cog_Extension

import time


class Help(Cog_Extension):
    @slash_command(invoke_without_command=True, name="help", description="協助中心")
    async def help(
        self, 
        ctx,
        類別: Option(str, "輸入指令類別", choices=["總覽", "聊天中心", "音樂中心", "用戶中心"])
    ):
        fromserver = ctx.author.guild.name
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("/help", 類別)
        print("from", fromserver)
        print("at", timestamp)
        print("by", ctx.author)
        print("------")

        if 類別 == "總覽" : 
            embed=discord.Embed(title="**HBYC的協助中心**", description="使用/help [類別] 取得該類別指令的詳細使用方法", color=0x0080FF)
            embed.set_author(name="HBYC#1512", icon_url="https://i.imgur.com/cuu63j3.jpg")
            embed.add_field(name="**指令類別總覽**", value="HBYC的指令類別總覽", inline=False)
            embed.add_field(name="🔵**聊天指令**", value="`/say`\n `/repeat`\n `/thinking`\n", inline=True)
            embed.add_field(name="🔵**音樂指令**", value="`/join`\n `/play`\n `/pause`\n `/resume`\n `/stop`\n", inline=True)
            embed.add_field(name="🔵**音樂指令**", value="`/avatar`\n `/report`\n" , inline=True)
            embed.set_footer(icon_url=ctx.author.avatar.url, text=f"{ctx.author} ‧ 使用/help [類別] 指令可取得更詳細的指令使用方式")
            await ctx.respond(embed=embed)
        
        if 類別 == "聊天中心" :
            embed=discord.Embed(title="🔴**聊天指令中心**", color=0x00A01D)
            embed.set_author(name="HBYC#1512", icon_url="https://i.imgur.com/cuu63j3.jpg")
            embed.add_field(name="`/say`", value="讓機器人替你說一句話", inline=False)
            embed.add_field(name="`/repeat`", value="讓機器人重複一句你說的話", inline=False)
            embed.add_field(name="`/thinking`", value="讓機器人送出一個thinking的表情符號", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar.url, text=f"{ctx.author} ‧ {timestamp}")
            await ctx.respond(embed=embed)

        if 類別 == "音樂中心" :
            embed=discord.Embed(title="🔴**音樂指令中心**", color=0xFF8000)
            embed.set_author(name="HBYC#1512", icon_url="https://i.imgur.com/cuu63j3.jpg")
            embed.add_field(name="`/join`", value="讓機器人加入你所在的語音頻道", inline=False)
            embed.add_field(name="`/leave`", value="讓機器人離開他所在的語音頻道", inline=False)
            embed.add_field(name="`/play`", value="讓機器人播放音樂，目前只能一次播放一首而且只能使用影片網址，音樂功能會在之後的版本再行改善", inline=False)
            embed.add_field(name="`/pause`", value="暫停正在播放的音樂", inline=False)
            embed.add_field(name="`/resume`", value="繼續播放原本在播放的音樂", inline=False)
            embed.add_field(name="`/stop`", value="結束目前正在播放的音樂", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar.url, text=f"{ctx.author} ‧ {timestamp}")
            await ctx.respond(embed=embed)

        if 類別 == "用戶中心" :
            embed = discord.Embed(title="🔴**用戶指令中心**", color=0x003cff)
            embed.set_author(name="HBYC#1512", icon_url="https://i.imgur.com/cuu63j3.jpg")
            embed.add_field(name="`/avatar`", value="讓機器人取得特定使用者的頭像", inline=False)
            embed.add_field(name="`/report`", value="傳送錯誤或建議回報給作者", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar.url, text=f"{ctx.author} ‧ {timestamp}")
            await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(Help(client))
    
