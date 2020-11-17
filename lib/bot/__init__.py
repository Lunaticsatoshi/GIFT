from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound
from discord import Embed, File
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glob import glob
from datetime import datetime 
from asyncio import sleep

PREFIX = "!"
OWNER_IDS = [572353145963806721]
COMMANDS = [path.split("\\")[-1][:-3] for path in glob("./lib/commands/*.py")]

class Ready(object):
    def __init__(self):
        for command in COMMANDS:
            setattr(self, command, False)
    def ready_up(self, command):
        setattr(self, command, True)
        print(f"{command} command is ready")

    def all_ready(self):
        return all([getattr(self, command) for command in COMMANDS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.command_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS)

    def setup(self):
        print("setup Run")
        for command in COMMANDS:
            self.load_extension(f"lib.commands.{command}") ## Checkn and Debug
            print(f"{command} cog Loaded")

    def run(self, version):
        self.VERSION = version
        print("running setup")
        self.setup()

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Gift Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def process_commands(self,message):
        ctx = await self.get_context(message, cls=Context)
        if ctx.command is not None and ctx.guild is not None:
            if self.ready:
                await self.invoke(ctx)
            else:
                await self.send("Wait for Oneechan to be ready!! ")
    
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

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        # elif hasattr(exc, "original"):
        #     raise exc.original
        else:
            raise exc


    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(710051662563115049)
            self.stdout = self.get_channel(710051662563115052)
            self.scheduler.start()
            while not self.command_ready.all_ready():
                print("waiting......")
                await sleep(0.5)
            self.ready = True
            print("Gift Bot ready")
            await self.stdout.send("Now Online")
        else:
            print("Gift Bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()