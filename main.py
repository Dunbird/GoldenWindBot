#Hid Token in Github
# TOKEN = ''
import asyncio
from webserver import keep_alive
import random
from discord.utils import get

#
import discord 
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from discord.ext.commands import check
#








client = commands.Bot(command_prefix = '?')

#tasks
status = cycle(['New Run Starting Soon', 'Remember to log in for daily rewards!','Remember to stay hydrated'])





#events

client.remove_command("help")

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server')

#commands 




##Starts MBC Run
@client.command()
@commands.has_role(727263364354670732)
async def mbc(ctx):
    msg = "A MBC run has been started by {0.author.mention} in the MBC channel \n Time Left:  \n To join, connect to the MBC channel by clicking its name and react with :mbc:  \n If you have a key, react with <:losthall:724419625265266689>  \n To indicate your class or gear choices, react with <:knight:724419485536223232> <:paladin:724419654281592832> <:warrior:724419907231678544> <:mseal:724419755661852674> <:puri:724419366254280844>  \n \n Time Remaining: \n \n Reactions \n  ".format(ctx.message)

    time_left = 5

    reactions = ['<:mbc:724418903220027453>','<:losthall:724419625265266689>' ,'<:knight:724419485536223232>', '<:paladin:724419654281592832>','<:warrior:724419907231678544>','<:mseal:724419755661852674>','<:puri:724419366254280844>']
    new_message = 'The AFK check has ended by {0.author.mention}  \n wait in lounge and wait for the new AFK check to start '.format(ctx.message)
    ## get the message
    message = ctx.message
    ## wait for 4 seconds again

    ## delete the message
    await message.delete()


    m = await ctx.send(msg)
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await m.add_reaction(emoji or name)
    #      await client.delete_message(message)
    await asyncio.sleep(300)
    await m.edit(content=new_message)
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await m.clear_reaction(emoji or name)


def in_voice_channel(): 
   # check to make sure ctx.author.voice.channel isnt 0 because if not then it wont work
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel
    return check(predicate)

##moves players into voice channel
@in_voice_channel()
@client.command()
@commands.has_role(727263364354670732)
async def move(ctx, *, channel : discord.VoiceChannel):
    for members in ctx.author.voice.channel.members:
            await members.move_to(channel)
    await asyncio.sleep(1)
    message = ctx.message
    await message.delete()


    








@client.command()
async def help(ctx):
  await ctx.send('Commands:\n Quote/quote\n crab\n family\n Most ARE case sensitive')

@client.command(aliases =['quote'] )
async def Quotes(ctx,):
  #Add responses below
  responses = [ 'Place Holder' ]
  await ctx.send(f'Here is a Random Quote from the Quotes Channel:\n {random.choice(responses)}')

@client.command()
async def ppe(ctx):
  responses = ['Rouge', ' Archer', 'Wizard', 'Priest', 'Warrior','Knight','Paladin','Assasin','Necromancer','Huntress','Mystic','Trickster','Sorcerer','Ninja','Samurai','Bard']
  await ctx.send(f'Your PPE class is {random.choice(responses)}')



@client.command()
async def family(ctx):
     await ctx.send(" BIight: Grandpa\n SunnyBPW: Mom\n Cody: Dad\n Golder:  Uncle\n Polnn: Uncle  \n Abyssssid: Cousin 1 \n LXbacon: Cousin 2 \n Cyborg:kid \n DrEvilOne and KingMikeI: Sunny's Kids \n SLAYERRVV: Gardener \n ")
     




@client.event
async def  on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    pass




#
@client.event
async def on_ready():
    change_status.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@tasks.loop(seconds=5)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))


keep_alive()
#client.run(TOKEN)