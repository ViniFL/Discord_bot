import discord
import os
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")


# from discord.ext import commands
# from discord.flags import Intents
# intents = discord.intents.all()

token1 = os.getenv("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!h':
            await message.channel.send(f'{message.author.name} os comandos do Bot são: {os.linesep} ?pl + link: Play {os.linesep} ?ps: Pausa {os.linesep} ?re: Replay no último link {os.linesep}')

       
client = MyClient()


