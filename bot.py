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

#Start the bot
client.run(TOKEN)
