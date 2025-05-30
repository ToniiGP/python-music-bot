import os
import discord
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#confirm bot is online
@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')

#Respond to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "ping":
        await message.channel.send("pong!")
    
    #Connecting bot ti voice channel in discord     
    elif message.content.lower() == "join":
        if message.author.voice:
            channel = message.author.voice.channel
            await channel.connect()
            await message.channel.send(f"Joined {channel.name}!!")
        else:
            await message.channel.send(f"You are not in a voice channel!")

#Start the bot
client.run(TOKEN)
