import random

# import os
# from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# load_dotenv()

BOT_TOKEN = "7506391433:AAFeARzQRDvGZ8xaiSUPSbPhFdycgAC041M"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

user_data: dict = {}


def gen_rand_int() -> int:
    return random.randint(1, 100)


def plain_start_text(message: Message) -> bool:
    return message.text == "/start"


@dp.message(plain_start_text)
async def process_start_command(message: Message):
    await message.answer(
        "Привет!\nПредлагаю сыграть в 'Угадай число'\n"
        "Узнать правила игры можно по команде /help\n"
        "Если хочешь сразу начать играть - напиши мне 'давай сыграем'"
    )

    if message.from_user.id not in user_data:
        user_data[message.from_user.id] = {
            "in_game": False,
            "secret_number": None,
            "attempts": None,
            "total_games": 0,
            "wins": 0,
        }


async def process_help_command(message: Message):
    await message.answer(
        "Правила игры:\n"
        "Я загадываю число от 1 до 100\n"
        "А тебе нужно его угадать.\n"
        f"У тебя есть {ATTEMPTS} попыток\n"
        "Доступные команды:\n"
        "/help - правила игры\n"
        "/cancel - выйти из игры\n"
        "/stat - посмотреть статистику\n"
        "\n\nСыграем?"
    )


async def process_stat_command(message: Message):
    await message.answer(
        f"Всего игр сыграно: {user_data[message.from_user.id].get('total_games')}\n"
        f"Игр выйграно: {user_data[message.from_user.id].get('wins')}"
    )


async def process_cancel_command(message: Message):
    if user_data[message.from_user.id].get("in_game"):
        user_data[message.from_user.id]["in_game"] = False
        await message.answer("Игра прервана\n" "Если захочешь сыграть - я тут!")
    else:
        await message.answer("А мы и так не играли\n" "Так может сыграем?")


@dp.message(
    F.text.lower().in_(["да", "давай", "сыграем", "давай сыграем", "погнали", "играть"])
)
async def process_positive_answer(message: Message):
    if not user_data[message.from_user.id].get("in_game"):
        user_data[message.from_user.id]["in_game"] = True
        user_data[message.from_user.id]["attempts"] = ATTEMPTS
        user_data[message.from_user.id]["secret_number"] = gen_rand_int()
        await message.answer("Начинаем игру!\nПопробуй угадать число!")
    else:
        await message.answer("Мы еще не закончили играть! Сначала угадай число!")


@dp.message(F.text.lower().in_(["нет", "не хочу", "не буду"]))
async def process_negative_answer(message: Message):
    if not user_data[message.from_user.id].get("in_game"):
        await message.answer("Хорошо. Когда захочешь поиграть - я тут")
    else:
        await message.answer("Мы уже в игре, так что играем!")


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
    if user_data[message.from_user.id].get("in_game"):
        if int(message.text) == user_data[message.from_user.id].get("secret_number"):
            user_data[message.from_user.id]["in_game"] = False
            user_data[message.from_user.id]["total_games"] += 1
            user_data[message.from_user.id]["wins"] += 1
            await message.answer("Молодец! Ты угадал число!\nСыграем еще?")
        elif int(message.text) < user_data[message.from_user.id].get("secret_number"):
            user_data[message.from_user.id]["attempts"] -= 1
            await message.answer("Загаданное число больше\nПопробуй еще раз!")
        elif int(message.text) > user_data[message.from_user.id].get("secret_number"):
            user_data[message.from_user.id]["attempts"] -= 1
            await message.answer("Загаданное число меньше\nПопробуй еще раз!")

        if user_data[message.from_user.id].get("attempts") == 0:
            user_data[message.from_user.id]["in_game"] = False
            user_data[message.from_user.id]["total_games"] += 1
            await message.answer(
                "Попыток больше нет..."
                f"Я загадал число {user_data[message.from_user.id].get('secret_number')}\n\n"
                "Сыграем еще раз? Напиши мне 'Давай сыграем'"
            )
    else:
        await message.answer("Мы еще не в игре. Сыграем?")


async def process_other_answer(message: Message):
    if user_data[message.from_user.id].get("in_game"):
        await message.answer(
            "Мы в игре! " "Угадай число или выйди из игры командой /cancel"
        )
    else:
        await message.answer("Давай просто поиграем в 'Угадай число?'")


# dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(process_stat_command, Command(commands="stat"))
dp.message.register(process_cancel_command, Command(commands="cancel"))
dp.message.register(process_other_answer)


if __name__ == "__main__":
    dp.run_polling(bot)
