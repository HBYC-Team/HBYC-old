import discord
from discord.commands import slash_command, Option
from core.classes import Cog_Extension

import time

timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Help(Cog_Extension):
    @slash_command(invoke_without_command=True, name="help", description="協助中心")
    async def help(
        self, 
        ctx,
        group: Option(str, "輸入指令類別", choices=["all", "chat", "music", "user"])
    ):
        if group == "all" : 
            embed=discord.Embed(title="HBYC的協助中心", description="使用/help [group] 取得該類別指令的詳細使用方法", color=0x0080FF)
            embed.add_field(name="指令類別", value="HBYC的指令類別", inline=False)
            embed.add_field(name="chat", value="say, repeat, thinking", inline=False)
            embed.add_field(name="music", value="join, play, pause, resume, stop", inline=False)
            embed.add_field(name="game", value="gn", inline=False)
            embed.set_footer(text=f"{ctx.author}‧{timestamp}")
            await ctx.respond(embed=embed)
        
        if group == "chat" :
            embed=discord.Embed(title="聊天指令類別", description="聊天指令", color=0x00A01D)
            embed.add_field(name="say", value="讓機器人替你說一句話", inline=False)
            embed.add_field(name="repeat", value="讓機器人重複一句你說的話", inline=False)
            embed.add_field(name="thinking", value="讓機器人送出一個thinking的表情符號", inline=False)
            embed.set_footer(text=f"{ctx.author}‧{timestamp}")
            await ctx.respond(embed=embed)

        if group == "music" :
            embed=discord.Embed(title="音樂指令類別", description="音樂指令", color=0xFF8000)
            embed.add_field(name="join", value="讓機器人加入你所在的語音頻道", inline=False)
            embed.add_field(name="leave", value="讓機器人離開他所在的語音頻道", inline=False)
            embed.add_field(name="play", value="讓機器人播放音樂，目前只能一次播放一首而且只能使用影片網址，音樂功能會在之後的版本再行改善", inline=False)
            embed.add_field(name="pause", value="暫停正在播放的音樂", inline=False)
            embed.add_field(name="resume", value="繼續播放原本在播放的音樂", inline=False)
            embed.add_field(name="stop", value="結束目前正在播放的音樂", inline=False)
            embed.set_footer(text=f"{ctx.author}‧{timestamp}")
            await ctx.respond(embed=embed)

        if group == "user" :
            embed = discord.Embed(title="使用者指令類別", description="使用者指令區", color="FF0000")
            embed.add_field(name="avatar", value="讓機器人取得特定使用者的頭像", inline=False)
            embed.set_footer(text=f"{ctx.author}‧{timestamp}")
            await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(Help(client))
    