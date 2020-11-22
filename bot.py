import discord
import event_handler
import os
import sys
from services import data
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv('discord_token')
if not discord_token:
    print('Discord token required for this application')
    sys.exit()

if not os.getenv('youtube_token'):
    print('Youtube token required for this application')
    sys.exit()
    
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: return
            
    if message.content.startswith(data.commands.get('movie_search')): 
        await event_handler.event_search_movie(message)


client.run(discord_token)
