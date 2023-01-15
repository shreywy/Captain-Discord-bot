import disnake, random
from disnake.ext import commands

# drizzy drake bot by sk8#5503
# this bot was designed for personal use

with open('token', 'r') as f:
    TOKEN = f.readline()

# sets up bots
bot = commands.Bot(
  command_prefix="[",#prefix, not needed for slash commands
  intents=disnake.Intents.all(),
  help_command=None,
  sync_commands_debug=True,
  test_guilds=[755459753068593314]
)

reply_dict = {}
keywords = []
quotes_list = []

# checks what servers this bot is in, saves info
def save_servers():
    guilds = bot.guilds
    guilds_list = str(guilds)[27:-3].split(', ')
    with open('servers', 'w') as f:
        for guild in guilds_list:
            f.write(str(guild) + '\n')

# pulls phrase/reactions from textreplies file
def get_replies():
    global reply_dict
    with open('textreplies', 'r') as f:
        texts = f.readlines()
    for line in texts:
        if line == '\n' or line == '': continue
        tempA, tempB = line.split('<,split,>')
        reply_dict[tempA.replace('\n', '')] = tempB.replace('\n', '')       
        global keywords
        if tempA not in keywords:
            keywords.append(tempA)

# get quotes from file
def get_quotes():
    global quotes_list
    with open('assets\quotes.txt', 'r') as f:
        quotes_list = f.readlines()
    

# startup events
@bot.event
async def on_ready():
    print('{0.user} has come to brampton'.format(bot))
    
    get_replies()
    
    global keywords
    keywords = list(reply_dict.keys())
    
    get_quotes()
    

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
    #respond to mesage text, gather text in startup function from file, store in dict.
    if not message.author.bot:
        for key in keywords:
            if key in user_message:
                await message.channel.send(reply_dict[key])
                return

#slash commands:

#anything to phrases/reactions
@bot.slash_command(name='add_words', description="add reactions to specified words or phrases")
async def add(inter, phrase: str, reaction: str):
    await inter.response.send_message(f'kk if i see a "{phrase}" then ill say "{reaction}"')
    with open('textreplies', 'a') as f:
        f.write(f'\n{phrase}<,split,>{reaction}')
    get_replies()

@bot.slash_command(name='remove_words', description="remove reactions to specified words or phrases")
async def add(inter, phrase: str):

    phrase = phrase
    global keywords
    if phrase in keywords:
        with open('textreplies', 'r') as f:
            text = f.readlines()
            
        with open('textreplies', 'w') as f:
            for line in text:
                if line.split('<,split,>')[0] == phrase:
                    continue
                else:
                    f.write(line)
            
        await inter.response.send_message(f'kk if i see a "{phrase}" then i wont say nun')
    else:
        await inter.response.send_message(f"don't tell me to breathe… bring me a shot. dawg this word wasnt even in the database yet")

@bot.slash_command(name='deep_quote', description="something from drizzy's most deepest quotes")
async def add(inter):
    global quotes_list
    await inter.response.send_message(random.choice(quotes_list))
    
@bot.slash_command(name='bot_info', description="info about bot")
async def add(inter):
    await inter.response.send_message('bot made by sk8#5503. say that you a lesbian, girl, me too')
    
# start bot
bot.run(TOKEN)