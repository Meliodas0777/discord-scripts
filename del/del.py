#!/usr/bin/python3
# Usage: .del (number) or .del 
import asyncio
import discord
import re

c = discord.Client()
token = "OTM0MjczMTE5ODQ4Mzc0MzMy.GUQW7A.Ga6Mfx6JHy8jF7uJQ3qgH2Qwd668vbDnv2rrL0"

@c.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}".format(c.user)
    print(welcome)

@c.event
async def on_message(message):
    if message.content.startswith('.del') and message.author == c.user:
        if re.search(r'\d+$', message.content) is not None:
            t = int(message.content[len('.del'):].strip())
        else:
            t = 9999
        async for m in message.channel.history(limit=t):
            try:
                if m.author == c.user:
                    await m.delete()
            except: pass

c.run(token, bot=False)
