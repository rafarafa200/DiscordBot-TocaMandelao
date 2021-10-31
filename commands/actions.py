from discord.ext import commands
from discord.errors import ClientException
import random

class Actions(commands.Cog):
    """Get Crypto data"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "join")
    async def join(self, ctx):
        try:
            if (ctx.author.voice):  # If the person is in a channel
                channel = ctx.author.voice.channel
                await channel.connect()
                print('Entrei')
                await ctx.send('Entrei, cusão!')
            else:                   #But is (s)he isn't in a voice channel
                await ctx.send("Você é burro? Você precisa estar e em um canal de voz para fazer isso!")
        except ClientException as e:
            print(e)
            await ctx.send("Já está conectado a um canal de voz!")

    @commands.command(name = "leave")
    async def leave(self, ctx): # Note: ?leave won't work, only ?~ will work unless you change  `name = ["~"]` to `aliases = ["~"]` so both can work.
        name = ctx.author.display_name
        
        if (ctx.voice_client): # If the bot is in a voice channel 
            await ctx.guild.voice_client.disconnect() # Leave the channel
            print('Sai')
            xingamentos = [ 
                            f'Flw, {name}, você tem uma senhora buceta!',
                            f'Tenho que vazar, não aguentei o tripe do {name}.',
                            f'Não fico na mesma call que o sulista {name}',
                            f'To saindo, vou comer o cu do {name}.',
                            f'Vou sair que hj tem festinha!',
                            f'Flw cabeça de cearense, {name}.',
                            f'Alá, o chupa cu: {name}',
                            f'Vlw, flw! {name}, xera bimba',
                            f'Flw, {name} tem uma senhora buceta',
                            f'Corre, o papa cu, {name}, está sedento!',
                            f'Adeus, vou chupar um anão!',
                            f'Ovo comer uma casada'
                            ]
            await ctx.send(xingamentos[random.randint(0, len(xingamentos)-1)])
        else: # But if it isn't
            await ctx.send("Você é burro? Eu preciso estar em um canal de voz!")
def setup(bot):
    bot.add_cog(Actions(bot))