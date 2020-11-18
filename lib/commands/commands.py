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
        

    # @command(name="roll", aliases=["Roll", "dice", "Dice"])
    # async def roll_dice(self, ctx, die_str: str):
    #     dice,value = (int(term) for term in die_str.split("d"))
    #     rolls = [randint(1,value) for i in range(dice)]
    #     await ctx.send(" + ".join([str(roll) for roll in rolls]) + f" = {sum(rolls)}")
        
    # @command(name="slap", aliases=["hit", "fuck"])
    # async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "existing"):
    #     await ctx.send(f"{ctx.author.display_name} slapped {member.mention} for {reason}")

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
