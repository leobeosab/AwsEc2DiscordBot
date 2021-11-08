import discord, boto3, config

client = discord.Client()
ec2 = boto3.resource('ec2')
instance = ec2.Instance(config.instance_id)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')


@client.event
async def on_message(message):
    if message.content.lower() == "stop":
        if turnOffInstance():
            await message.channel.send('AWS Instance stopping')
        else:
            await message.channel.send('Error stopping AWS Instance')
    elif message.content.lower() == "start":
        if turnOnInstance():
            await message.channel.send('AWS Instance starting')
        else:
            await message.channel.send('Error starting AWS Instance')
    elif message.content.lower() == "state":
        if getInstanceState():
            await message.channel.send('AWS Instance state is: ' + getInstanceState())
    elif message.content.lower() == "reboot":
        if rebootInstance():
            await message.channel.send('AWS Instance rebooting')
        else:
            await message.channel.send('Error rebooting AWS Instance')
    elif message.content.lower() == "test":
        await message.channel.send('Thanks, Jace. Helps alot.')

def turnOffInstance():
    try:
        instance.stop()
        return True
    except:
        return False

def turnOnInstance():
    try:
        instance.start()
        return True
    except:
        return False

def getInstanceState():
        return instance.state['Name']

def rebootInstance():
    try:
        instance.reboot()
        return True
    except:
        return False

client.run(config.discord_key)