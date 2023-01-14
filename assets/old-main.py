# original bot script used to make something basic
'''
import disnake as discord
from disnake import *

with open('token', 'r') as f:
    TOKEN = f.readline()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def save_servers():
    guilds = client.guilds
    guilds_list = str(guilds)[27:-3].split(', ')
    with open('servers', 'w') as f:
        for guild in guilds_list:
            f.write(str(guild) + '\n')

@client.event
async def on_ready():
    print('papi\'s home - {0.user}'.format(client))
    #save_servers()

@client.event
async def on_message(message):
    #message info
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #console chat log
    print(f'{username}: {user_message} ({channel})')    
    
    #so the bot doesnt reply to itself
    if message.author == client.user or message.author.bot:
        return
    
    #text replies
    if 'wysi' in user_message:
        await message.channel.send('bro saw 727 :skull:')
        
    if 'greninja' in user_message:
        await message.channel.send('https://images-ext-1.discordapp.net/external/5ftDMrD24EHqpB8gT2R1tfybkjosJVrzPDEUiPJxOC4/%3Fsize%3D240%26quality%3Dlossless/https/cdn.discordapp.com/emojis/1043737485232050237.webp')

    if 'turban' == user_message:
        await message.channel.send('https://cdn.discordapp.com/attachments/768197262546960415/1063242422328512552/bramalea.rd_20210409_144416_0.mp4')

    #voice chat
    if user_message == ']join':
        channel = message.author.voice.channel
        await channel.connect()
  
    if user_message == ']dc':
        voice_client = message.guild.voice_client
        await voice_client.disconnect()
       
    if user_message == ']icespice':
        voice_client = message.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(executable='C:\\Users\\Shrey\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg', source='assets\munch.mp3'))


client.run(TOKEN)'''