import discord

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
    save_servers()

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    
    print(f'{username}: {user_message} ({channel})')    
    
    if message.author == client.user or message.author.bot:
        return
    
    if 'wysi' in user_message:
        await message.channel.send('bro saw 727 :skull:')


client.run(TOKEN)