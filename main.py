# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

my_id = 463447025048879104
blacklist = [328177046956015616]




@bot.event
async def on_voice_state_update(member, before, after):
    # checking if event was not disconnect
    if after.channel is None:
        return
    
    # checking if i am in voice from event
    im_in_voice = False
    
    for voice_member in after.channel.members:
        if voice_member.id == my_id:
            im_in_voice = True
            
    if not im_in_voice:
        return
    
    # checking if member is blacklisted and kick him
    for voice_member in after.channel.members:
        if voice_member.id in blacklist:
            print(f"Kicking {voice_member}!")
            await voice_member.edit(voice_channel=None, reason="[001] > Not compatible!")

bot.run(token=os.getenv('TOKEN'))
