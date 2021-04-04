import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg_full = message.content
    msg = msg_full.strip()
    if msg=="あ" or msg=="ㅏ" or msg=="아" or msg.lower()=="a" or msg == "ア":
        await message.add_reaction("🦈")
    if msg_full.find("🦈") > -1:
        await message.add_reaction("🅰️")

keep_alive()
client.run(os.getenv("TOKEN"))