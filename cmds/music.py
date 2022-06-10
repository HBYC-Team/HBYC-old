from discord.commands import slash_command, Option
from core.classes import Cog_Extension
from discord.utils import get
from discord import ApplicationCommand, FFmpegPCMAudio
from youtube_dl import YoutubeDL

import json

with open("config.json", mode="r", encoding="utf8") as jfile:
    config = json.load(jfile)

class Music(Cog_Extension):
    @slash_command(name="join", description="讓機器人加入你所在的語音頻道")
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        
        if ctx.author.voice.channel is None:
            await ctx.respond("請先加入一個語音頻道")

        if voice and voice.is_connected():
            await voice.move_to(channel)
            await ctx.respond(f"已加入`{channel}`")
        else:
            voice = await channel.connect()
            await ctx.respond(f"已加入`{channel}`")


    @slash_command(name="leave", description="讓機器人離開他所在的語音頻道")
    async def leave(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.respond("✅")

        else:
            await ctx.respond("我並不在任何語音頻道中")

    @slash_command(name="play", description="讓機器人播放音樂，目前只能一次播放一首而且只能使用影片網址，音樂功能會在之後的版本再行改善")
    async def play(self, 
        ctx, 
        url: Option(str, "請將連結貼在這裡")
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

        else:
            await ctx.respond("我已經在播音樂了！")
            return
    

    @slash_command(name="resume", description="繼續播放原本在播放的音樂")
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.respond("✅")


    @slash_command(name="pause", description="暫停正在播放的音樂")
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.respond("✅")


    @slash_command(name="stop", description="結束目前正在播放的音樂")
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.respond("✅")


def setup(bot):
    bot.add_cog(Music(bot))