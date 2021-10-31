from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from discord.errors import ClientException
import discord
import os
import yt_dlp
import urllib.parse, urllib.request, re

class Music(commands.Cog):
    """Get Crypto data"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="p")
    async def play(self, ctx, *, url):
        song_there = os.path.isfile(os.getcwd() + "\\song.mp3")
        try:
            if song_there:
                os.remove(os.getcwd() + "\\song.mp3")
        except PermissionError as e:
            print(f"Erro de permissão: {e}")
            await ctx.send("Pera a musica acabar")

        channel = ctx.author.voice.channel
        try:
            await channel.connect()
        except ClientException:
            await ctx.send("Pera a musica acabar")
        except CommandInvokeError:
            await ctx.send("Entra no canal, sua mula!")

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

        if "https://www.youtube.com/" in url:
            pass
        else:
            query_string = urllib.parse.urlencode({
            'search_query': url
            })
            htm_content = urllib.request.urlopen(
                "https://www.youtube.com/results?" + query_string
            )

            search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
            url = "http://www.youtube.com/watch?v=" + search_results[0]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir():
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            await ctx.send("Tocando Agora: " + url)
        except Exception as e:
            await ctx.send(f"Ops, deu um pobrema! Erro: {e}")

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Não tá tocando nada, sua anta!")

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Não tem música pra pausar, sua besta!")

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()

    @commands.command(name="s")
    async def search(self, ctx, *, search):
        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        
        htm_content = urllib.request.urlopen(
            "https://www.youtube.com/results?" + query_string
        )

        search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
        results = ["http://www.youtube.com/watch?v=" + search_results[i] for i in range(len(search_results))]
        
        embed_search = discord.Embed(
            title = "Resultados da Pesquisa",
            color = 0x0000FF
        )
        results = results[:6]
        for i, result in enumerate(results):
            embed_search.add_field(name=f"{i+1})", value=result)
        embed_search.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed = embed_search)

def setup(bot):
    bot.add_cog(Music(bot))