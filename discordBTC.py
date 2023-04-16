# This example requires the 'message_content' intent.

import discord
import os
import openai
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message.content},
    ]
    )

    await message.channel.send(completion.choices[0].message['content'])
    # if message.content.startswith('$hello'):
    #    await message.channel.send('Hello!')
# send message to a specific channel
# channel = client.get_channel(CHANNEL_ID)
# await channel.send('Hello!')
# Integrate with Lnbits wallet API
#
#
# Integrate with lnurl-pay
#
#
# Integrate with lnurl-withdraw
#
#
# Integrate with lnurl-auth
#
#
# Integrate with lnd
#
#
# Integrate with c-lightning
#
#
# Integ



client.run(os.getenv("DISCORD_TOKEN"))

