from discord.ext import commands

class Reactions(commands.Cog):
    """Reactions to user"""
    def __init__(self, bot):
        self.bot = bot

    #events ==> commands.Cog.listener
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == ":thumbsup:":
            #adicionar o código da role
            role = user.guild.get_role()
            await user.add_roles(role)
        elif reaction.emoji == ":poop:":
            role = user.guild.get_role()
            await user.add_roles(role)
            

def setup(bot):
    bot.add_cog(Reactions(bot))