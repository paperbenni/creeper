import discord
import os

if os.path.exists('.token'):
    discordtoken = open('.token', 'r').read()
    print(discordtoken)
else:
    discordtoken = os.environ['DISCORD']

client = discord.Client()

revenge = open("revenge.txt", "r").read().lower().replace(
    '\n', ' ').split(' ')
print(revenge)
creepercounter = 0


@client.event
async def on_ready():
    print('Logged in as {} Creeper Aww man'.format(client.user))


@client.event
async def on_message(message):
    if message.author == client.user:
        print("my message")
        return

    mcontent = message.content.lower().replace(
        '-', ' ').replace('\'', '').replace('.', '').replace(',', '').replace('\n', '')
    mlist = mcontent.split(' ')
    global creepercounter
    print(mlist)

    for i in mlist:
        if revenge[creepercounter] == i:
            creepercounter += 1
        else:
            creepercounter = 0
            await message.channel.send('you fuked up')
            break
    if creepercounter != 0:
        if mcontent != 'creeper':
            print(revenge[creepercounter])
            creeperstring = ''
            for i in range(3):
                creeperstring += (" " + revenge[creepercounter])
                creepercounter += 1
            await message.channel.send(creeperstring)
        else:
            creepercounter += 2
client.run(discordtoken)
