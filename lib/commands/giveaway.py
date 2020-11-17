from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Member
from typing import Optional
from random import choice, randint

class Giveaway(Cog):
    def __init__(self,bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.command_ready.ready_up("giveaway")

def setup(bot):
    bot.add_cog(Giveaway(bot))