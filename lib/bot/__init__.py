from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound
from discord import Embed, File
from datetime import datetime 
from asyncio import sleep

PREFIX = "!"
OWNER_IDS = [572353145963806721]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token","r") as tf:
            self.TOKEN = tf.read()

        print("Running Gift Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Ara Ara!")

    async def on_disconnect(self):
        print("Ara Ara Sionara!")

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_command_error':
            await args[0].send("Somthing went wrong.")
        channel = self.get_channel(710051662563115052)
        await channel.send("An error Occurrred")
        raise 

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(710051662563115049)
            self.stdout = self.get_channel(710051662563115052)

            self.ready = True
            print("Gift Bot Ready")
            await self.stdout.send("Now Online!!")

        else:
            print("Gift Bot Reconnected")


bot = Bot()