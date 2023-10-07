import logging
import time
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

typing = 0

class CustomClass:
    pass

logging.basicConfig(filename='logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.getLogger().addHandler(console_handler)

import discord

bot = discord.Bot()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.reference:
        referenced_message = await message.channel.fetch_message(message.reference.message_id)
    else:
        referenced_message = CustomClass()
        referenced_message.author = None
    if f'<@{bot.user.id}>' in message.content or referenced_message.author == bot.user:
        await message.add_reaction('💭')
        async with message.channel.typing():
            global typing
            if typing != 1:
                typing = 1
            else:
                while True:
                    if typing != 1:
                        break
                    await asyncio.sleep(0.5)
            if referenced_message.author != None:
                response = input(f'{message.author} replied to message {referenced_message.author}:"""{referenced_message.content}""" Enter response: {message.content} ((RESPONSE > ')
            else:
                response = input(f'{message.author}: {message.content} ((RESPONSE > ')
            await message.reply(response)
            message = await message.channel.fetch_message(message.id)
            bot_user = await bot.fetch_user(bot.user.id)
            reaction = discord.utils.get(message.reactions, emoji='💭')
            typing = 0
        while True:
            if reaction:
                await reaction.remove(bot_user)
                break
            asyncio.sleep(0.5)


@bot.event
async def on_ready():
    logging.info('Ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="questions && Responding to them"))
    

bot.run(bot_token)
