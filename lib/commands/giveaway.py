import discord
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions
from discord import Member
from discord import Embed, File
from typing import Optional
from random import choice, randint
from asyncio import TimeoutError, sleep
from lib.util.util import convert

class Giveaway(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="giftcr", aliases=["giveaway", "gcreate", "gcr"])
    @has_permissions(manage_guild=True)
    async def create_giveaway(self, ctx):
        embed = Embed(title="Giveaway Time!!✨",
                      description="Time for a new Giveaway. Answer the following questions in 25 seconds each for the Giveaway",
                      color=ctx.author.color)
        await ctx.send(embed=embed)
        questions=["In Which channel do you want to host the giveaway?",
                   "For How long should the Giveaway be hosted ? type number followed (s|m|h|d)",
                   "What is the Prize?"]
        answers = []
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        for i, question in enumerate(questions):
            embed = Embed(title=f"Question{i}",
                          description=question)
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', timeout=25, check=check)
            except TimeoutError:
                await ctx.send("You didn't answer the questions in Time")
                return
            answers.append(message.content)
        try:
            # print(int(answers[0][2:-1]))
            channel_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"The Channel provided was wrong. The channel should be {ctx.channel.mention}")
            return

        channel = self.bot.get_channel(channel_id)
        time = convert(answers[1])
        if time == -1:
            await ctx.send("The Time format was wrong")
            return
        elif time == -2:
            await ctx.send("The Time was not conventional number")
            return
        prize = answers[2]

        await ctx.send(f"Your giveaway will be hosted in {channel.mention} and will last for {answers[1]}")
        embed = Embed(title="Giveaway Time !!",
                    description=f"Win a {prize} today")
        embed.add_field(name="Hosted By:", value=ctx.author.mention)
        embed.set_footer(text=f"Giveway ends in {answers[1]} from now")
        newMsg = await channel.send(embed=embed)
        await newMsg.add_reaction("🎉")
        await sleep(time)

        myMsg = await channel.fetch_message(newMsg.id)

        users = await myMsg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = choice(users)
        await channel.send(f"Congratulations {winner.mention} on winning {prize}")

    @command(name="giftrrl", aliases=["greroll", "giveroll", "grr"])
    @has_permissions(manage_guild=True)
    async def giveaway_reroll(self, ctx, channel : discord.TextChannel, id_: int):
        try:
            msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The ID was incorrect")
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = choice(users)
        await channel.send(f"Congratulations {winner.mention} on winning the Giveaway")
        pass


    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.command_ready.ready_up("giveaway")

def setup(bot):
    bot.add_cog(Giveaway(bot))