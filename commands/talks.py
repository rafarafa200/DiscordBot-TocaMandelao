from discord.ext import commands

class Talks(commands.Cog):
    """Talks to user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi")
    async def send_hello(self, ctx):
        name = ctx.author.display_name
        response = "Salve, bundão, " + name
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Talks(bot))