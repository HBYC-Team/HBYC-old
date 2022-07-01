import discord
from discord.ext import commands, bridge
from discord.commands import slash_command, Option
from core.classes import Cog_Extension
from discord.utils import get
from discord import ApplicationCommand, FFmpegPCMAudio
from youtube_dl import YoutubeDL

import json, time

with open("config.json", mode="r", encoding="utf8") as jfile:
    config = json.load(jfile)


class Music(Cog_Extension):
    @bridge.bridge_command(name="join", description="讓機器人加入你所在的語音頻道")
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.respond("請先加入一個語音頻道")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()
        await ctx.respond(f"已加入`{ctx.author.voice.channel}`")
        fromserver = ctx.author.guild.name
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("/join")
        print("from", fromserver)
        print("at", timestamp)
        print("by", ctx.author)
        print("------")

    @bridge.bridge_command(name="leave", description="讓機器人離開他所在的語音頻道")
    async def leave(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.respond(f"已離開`{ctx.author.voice.channel}`")
            fromserver = ctx.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("/leave")
            print("from", fromserver)
            print("at", timestamp)
            print("by", ctx.author)
            print("------")

        else:
            await ctx.respond(f"{ctx.author.mention} 我並不在任何語音頻道中")

    @bridge.bridge_command(name="play", description="讓機器人播放音樂，目前只能一次播放一首而且只能使用影片網址，音樂功能會在之後的版本再行改善")
    @discord.option(name="url", type=str)
    async def play(self, 
        ctx, 
        url: "請將連結貼在這裡"
    ):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            now_playing = f"現正播放：{url}"
            await ctx.respond(now_playing)
            fromserver = ctx.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("/play", url)
            print("from", fromserver)
            print("at", timestamp)
            print("by", ctx.author)
            print("------")

        else:
            await ctx.respond(f"{ctx.author.mention}我已經在播音樂了！")
            return
        

    @bridge.bridge_command(name="resume", description="繼續播放原本在播放的音樂")
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.respond("繼續播放音樂")
            fromserver = ctx.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("/resume")
            print("from", fromserver)
            print("at", timestamp)
            print("by", ctx.author)
            print("------")
        
        else:
            await ctx.respond(f"{ctx.author.mention} 我根本沒有在播音樂")
            
    @bridge.bridge_command(name="pause", description="暫停正在播放的音樂")
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.respond("暫停播放音樂")
            fromserver = ctx.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("/pause")
            print("from", fromserver)
            print("at", timestamp)
            print("by", ctx.author)
            print("------")

    @bridge.bridge_command(name="stop", description="結束目前正在播放的音樂")
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.respond(f"{ctx.author.mention} 音樂已停止")
            fromserver = ctx.author.guild.name
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("/stop")
            print("from", fromserver)
            print("at", timestamp)
            print("by", ctx.author)
            print("------")
        
        else:
            await ctx.respond(f"{ctx.author.mention} 我根本沒有在播音樂")

def setup(client):
    client.add_cog(Music(client))