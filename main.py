import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import BaseFilter

import time


BOT_TOKEN = "7506391433:AAFeARzQRDvGZ8xaiSUPSbPhFdycgAC041M"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


admin_ids: list[int] = [868563700]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def asnwer_if_admins_update(message: Message):
    await message.answer(text='Admin')


@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Not Admin')


# async def one():
#     print("Hello world. Function One started")
#     await asyncio.sleep(1)
#     print("Function one: I'm here")


# async def two():
#     print("Hello there. Function two is here")
#     await asyncio.sleep(2)
#     print("Function two: what's up?")


# async def main():
#     asyncio.create_task(one())
#     await asyncio.create_task(two())


if __name__ == "__main__":
    dp.run_polling(bot)
