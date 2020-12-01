from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, File
from random import choice

class Command(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="hello", aliases=["hola", "h"], hidden=True)
    async def say_hello(self, ctx):
        await ctx.send(f"{choice(('Konnichiva', 'Ara Ara', 'Okaeri', 'Yahallo'))} {ctx.author.mention}!")

    # @command(name="echo", aliases=["say", "shout"])
    # async def echo_message(self, ctx, *, message):
    #     await ctx.message.delete()
    #     await ctx.send(message)

    @command(name="gifth", aliases=["ghelp", "gifhelp", "givehelp"])
    async def help_user(self, ctx):
        embed = Embed(title="Giveaway setup Help",
                      description="Setup Your giveaway in some simple commands",
                      color=ctx.author.color)
        embed.add_field(name="Create Giveaway", value="Create a giveaway by using the !giveaway command. Additionally you can also use commands like !giftcr or !gcreate. The bot will ask some simple questions to host your giveaway")
        embed.add_field(name="Reroll Giveaway", value="Reroll a giveaway again by using the !gifreroll command. Additionally you can also use commands like !gftroll or !giftrrl. The bot will ask some simple questions to host your giveaway")
        embed.add_field(name="Cancel Giveaway", value="Delete a giveaway by using the !giftdel command. Additionally you can also use commands like !gftdel or !gifdel. The bot will ask some simple questions to host your giveaway")
        await ctx.send(embed=embed)
    
    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.command_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
