import logging
import time
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
user_id = os.getenv('USER_ID')
emoji = os.getenv('EMOJI')
timeout = int(os.getenv('TIMEOUT_SECONDS'))
errormessage = os.getenv('ERROR_MESSAGE')

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
    response = CustomClass()
    if message.author == bot.user:
        return
    if message.reference:
        referenced_message = await message.channel.fetch_message(message.reference.message_id)
    else:
        referenced_message = CustomClass()
        referenced_message.author = None
    if f'<@{bot.user.id}>' in message.content or referenced_message.author == bot.user:
        await message.add_reaction(emoji)
        async with message.channel.typing():
            global typing
            if typing != 1:
                typing = 1
            else:
                while True:
                    if typing != 1:
                        break
                    await asyncio.sleep(0.5)
            user = await bot.fetch_user(user_id)
            def check(response):
                return response.author == user and response.channel == user.dm_channel
            if referenced_message.author != None:
                try:
                    logging.info(f'An user has interacted with the bot ({message.author} replying to {referenced_message.author}: {message.content})')
                    await user.send(f'{message.author.mention} replied to message from {referenced_message.author.mention}:"""{referenced_message.content}""" The message is: {message.content}')
                    response = await bot.wait_for('message', check=check, timeout=timeout)
                except asyncio.TimeoutError:
                    logging.warning(f'Timeout occured, didn\'t give a response for {timeout} seconds.')
                    response.content = errormessage
                except Exception as e:
                    logging.error(e)
                    response.content = errormessage
            else:
                try:
                    logging.info(f'An user has interacted with the bot ({message.author}: {message.content})')
                    await user.send(f'{message.author.mention}: {message.content}')
                    response = await bot.wait_for('message', check=check, timeout=timeout)
                except asyncio.TimeoutError:
                    logging.warning(f'Timeout occured, didn\'t give a response for {timeout} seconds.')
                    response.content = errormessage
                except Exception as e:
                    logging.error(e)
                    response.content = errormessage
            await message.reply(response.content)
            message = await message.channel.fetch_message(message.id)
            bot_user = await bot.fetch_user(bot.user.id)
            reaction = 1
            typing = 0
        while True:
            if reaction:
                await message.remove_reaction(emoji, bot_user)
                reaction = 0
                break
            asyncio.sleep(0.1)


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}, ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='questions && Responding to them'))

bot.run(bot_token)
