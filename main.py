import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
listOfPlayers = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def queue(ctx):

    str1 = '__**Current CSGO Queue**__\n'
    str2 = ''
    if len(listOfPlayers) == 0:
        await ctx.send(str1 + 'No players currently in the queue.')
    else:
        for num, player in enumerate(listOfPlayers, start=1):
            str2 += '{}: {}\n'.format(num, player.name)
        await ctx.send(str1 + str2)


@client.command()
async def play(ctx):
    player = ctx.author
    str1 = "Get your snacks, it's game time!\n"
    str2 = ''

    if 1 in listOfPlayers:
        await ctx.send('You are already in the queue.')
    elif len(listOfPlayers) > 4:
        await ctx.send('Queue is full')
    else:
        await ctx.send(f'You are added to the queue.\n{player.name} wants to play!')
        listOfPlayers.append(player)
        if len(listOfPlayers) == 5:
            for p in listOfPlayers:
                str2 += f'{p.mention}, '
            await ctx.send(str1 + str2)
            listOfPlayers.clear()


@client.command()
async def leave(ctx):
    player = ctx.author
    if player in listOfPlayers:
        listOfPlayers.remove(player)
        await ctx.send('You left the queue.')
    else:
        await ctx.send('You are not currently in the queue')


@client.command()
async def flush(ctx):
    await ctx.send('Queue cleared.')
    listOfPlayers.clear()

client.run('Nzk0OTAyMDQ4NTQ0OTE1NDc2.X_BkOA.MfL8FSnsAIJkgBh3MF-C3L1lixY')
