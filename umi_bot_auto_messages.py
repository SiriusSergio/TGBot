# import requests

import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()

# API_URL = "https://api.telegram.org/bot"
# API_CATS_URL = "https://api.thecatapi.com/v1/images/search"
BOT_TOKEN = os.getenv("BOT_TOKEN")
TEXT = "Hi, I'm Umi and you're warm!"
# ERROR_TEXT = "Cat is missing at the moment..."
# MAX_COUNTER = 100

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer(TEXT)


async def process_help_command(message: Message):
    await message.answer("I'm always here with you")


async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)


async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)

# offset = -2
# counter = 0
# chat_id: int
# cat_responce: requests.Response
# cat_link: str

# while counter < MAX_COUNTER:

#     print('attempt =', counter)

#     updates = requests.get(
#         f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}'
#         ).json()

#     print(updates)

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_responce = requests.get(API_CATS_URL)
#             if cat_responce.status_code == 200:
#                 cat_link = cat_responce.json()[0]['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

#             time.sleep(1)
#             counter += 1
