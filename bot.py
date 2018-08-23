import discord, asyncio, os, boto3

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

@client.event
async def on_message(message):
    memberIDs = (member.id for member in message.mentions)
    if client.user.id in memberIDs:
        await client.send_message(message.channel, 'you rang?')

client.run(os.environ['AWSDISCORDTOKEN'])
