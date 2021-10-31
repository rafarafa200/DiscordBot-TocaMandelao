from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manage the bot"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou Pronto! Conectado como: {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os Argumentos!")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe!")
        else:
            raise error
def setup(bot):
    bot.add_cog(Manager(bot))