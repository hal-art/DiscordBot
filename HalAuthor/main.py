import discord
import os
from log import log
from log import LogLevel
from dotenv import load_dotenv

load_dotenv()
client = discord.Client(intents=discord.Intents.default())

TOKEN = os.getenv('TOKEN')
CHANNELID = (int)(os.getenv('CHANNELID'))

@client.event
async def on_ready():
    log("初期化完了", LogLevel.INFO)

@client.event
async def on_message(message):
    if not message.author.bot:
        channel = client.get_channel(CHANNELID)
        await channel.send("こんにちは!")
        print(message.content)
client.run(TOKEN)