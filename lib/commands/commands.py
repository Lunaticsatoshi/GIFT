from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Member
from typing import Optional
from random import choice, randint

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

    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.command_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
