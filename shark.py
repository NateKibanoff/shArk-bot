import discord
import os
from keep_alive import keep_alive
import random
import re

client = discord.Client()

a = ["a", "A", "@", "あ", "ア", "ㅏ", "아"]

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	msg_full = message.content
	rng = random.randint(1,8)
	if msg_full.strip() in a or re.search("^[Aa@あアㅏ아]+[h!?.]*$", msg_full.strip().lower()) is not None:
		await message.add_reaction("🦈")
	if msg_full.find("🦈") > -1:
		await message.add_reaction("🅰️")
	if msg_full.lower().find("fireball") > -1 and rng == 1:
		await message.channel.send("DID SOMEONE SAY FIREBALL?")
	if msg_full.lower().find("wraith lord") > -1 and rng <= 2:
		await message.channel.send("DID SOMEONE SAY WRAITH LORD?")

keep_alive()
client.run(os.getenv("TOKEN"))