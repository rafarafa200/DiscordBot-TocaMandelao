from discord.ext import commands
import discord

class Smarts(commands.Cog):
    """Smart commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calcular")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)

        #Alterar o eval
        response = expression

        embed_image = discord.Embed(
                title="Segundo Glaucio Terra", 
                description="...", 
                color=0x00ff00
                )
        
        file = discord.File("imgs/pensador.jpeg", filename="image.jpeg")
        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.add_field(name="Pensando", inline=False, value='...')
        embed_image.set_image(url="attachment://image.jpeg")
        await ctx.send(file=file, embed=embed_image)
        
        embed_resp = discord.Embed(
                title="Resposta: ",
                description=str(response),
                color=0x00ff00
                )
        await ctx.send(embed=embed_resp)

def setup(bot):
    bot.add_cog(Smarts(bot))