import discord
import time
import datetime
import asyncio
from colorama import Fore
import os
import requests
from discord.ext import commands
from discord.utils import get
from os import system
from discord.ext import commands
from random import choice as randchoices
import platform
### i dont think i need all these import made this at night time lol







token = input("Enter token you wanna host : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)


if src.status_code == 200:
    print('Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
    input("Press any key")




client = commands.Bot(command_prefix=".", self_bot=True)
ready = False

system('title ' + 'LOGGER')

start_time = datetime.datetime.utcnow()

BOT_PREFIX = 'x'






client = commands.Bot(command_prefix=BOT_PREFIX, self_bot=True)








system('title ' + ' lol')

start_time = datetime.datetime.utcnow()
os = platform.system()

if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(f'''{Fore.RED}



             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    


══════════════════════════════════════════════════
    MENTION LOGGER: ENABLED                                                  
══════════════════════════════════════════════════


   
                           ''' + Fore.RESET)
@client.event
async def on_connect():
    
    print(
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Version: {discord.__version__}\n'
    )





















###HELP EMBED 





client.remove_command('help')
@client.command()
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=0x1f8b4c, timestamp=ctx.message.created_at)
 embed=discord.Embed(title="𝘴𝘩𝘢𝘮", color=0x000000)
 embed.set_thumbnail(url="https://media.discordapp.net/attachments/749509994944397313/769795615894405149/image0.gif?width=654&height=654")
 embed.add_field(name="𝙝𝙚𝙡𝙥 𝙘𝙢𝙙𝙨", value="𝙙𝙞𝙨𝙥𝙡𝙖𝙮𝙨 𝙩𝙝𝙚 𝙝𝙚𝙡𝙥 𝙤𝙥𝙩𝙞𝙤𝙣𝙨", inline=False)
 embed.add_field(name="𝙪𝙩𝙞𝙡 𝙘𝙢𝙙𝙨", value="𝙪𝙩𝙞𝙡𝙞𝙩𝙮 𝙨𝙝𝙞𝙩", inline=False)
 embed.add_field(name="𝙛𝙪𝙣 𝙘𝙢𝙙𝙨", value="𝙛𝙪𝙣 𝙨𝙝𝙞𝙩", inline=False)
 embed.add_field(name="𝙣𝙨𝙛𝙬 𝙘𝙢𝙙𝙨", value="𝙣𝙤𝙩 𝙛𝙤𝙧 𝙠𝙞𝙙𝙨 𝙡𝙤𝙡", inline=False)
 embed.add_field(name="𝙘𝙧𝙚𝙙𝙞𝙩𝙨", value="𝙜𝙞𝙫𝙚𝙨 𝙖𝙡𝙡 𝙘𝙧𝙚𝙙𝙞𝙩𝙨 𝙛𝙤𝙧 𝙘𝙧𝙚𝙖𝙩𝙤𝙧 𝙤𝙛 𝙩𝙝𝙞𝙨", inline=False)
 await ctx.send(embed=embed)


























                          



@client.listen('on_message')
async def ifmentioned(message):
    if message.author == client.user:
        return
    if str(client.user.id) in message.content:
        print("══════════════════════════════════════════════════")
        print(Fore.RED + "[Mentioned] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"You were mentioned by {message.author} ." + Fore.RESET)
        print(Fore.BLUE + "[Mentioned] " + Fore.RESET + Fore.RED + f"Server: {message.guild}" + Fore.RESET)
        print(Fore.BLUE + "[Mentioned] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}")
        print(Fore.RED + "[Mentioned] " + Fore.RESET + Fore.WHITE + f"Message Content: {message.content}".replace(f"<@{client.user.id}>" or f"<@!{client.user.id}>", "") + Fore.RESET)
        print("══════════════════════════════════════════════════")












#####################################################SELFBOT COMMANDS WILL BE WORKED ON LATER ON to lazy rn






client.run(token, bot=False)