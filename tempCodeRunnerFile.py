import disnake
from disnake.ext import commands

with open('token', 'r') as f:
    TOKEN = f.readline()

'''intents = disnake.Intents.default()
intents.message_content = True
bot = disnake.bot(intents=intents)

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True'''

bot = commands.Bot(
  command_prefix="!",#prefix, not needed for slash commands
  intents=disnake.Intents.all(),
  help_command=None, #in case you want to add your own help command
  sync_commands_debug=True,
  test_guilds=[755459753068593314]
)

reply_dict = {}
keywords = []


def save_servers():
    guilds = bot.guilds
    guilds_list = str(guilds)[27:-3].split(', ')
    with open('servers', 'w') as f:
        for guild in guilds_list:
            f.write(str(guild) + '\n')

def get_replies():
    global reply_dict
    with open('textreplies', 'r') as f:
        texts = f.readlines()
    for line in texts:
        tempA, tempB = line.split('<,split,>')
        reply_dict[tempA.replace('\n', '')] = tempB.replace('\n', '')

@bot.event
async def on_ready():
    print('papi\'s home - {0.user}'.format(bot))
    
    global reply_dict
    get_replies()
    
    global keywords
    keywords = list(reply_dict.keys())

@bot.event
async def on_message(message):
    #message info
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #console chat log
    print(f'{username}: {user_message} ({channel})')    
    
    #so the bot doesnt reply to itself
    if message.author == bot.user or message.author.bot:
        return
    
    #text replies
    #TODO: respond to mesage text, gather text in startup function from file, store in dict.
    for key in keywords:
        if key in user_message:
            await message.channel.send(reply_dict[key])
            return

    

@bot.slash_command(name='hello', description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")
    
'''@bot.slash_command(name='add words', description="add reactions to specified words or phrases")
async def add(inter, react_to: str, reaction: str):
    await inter.response.send_message(f"kk if i see a {react_to} then ill say {reaction}")'''

bot.run(TOKEN)