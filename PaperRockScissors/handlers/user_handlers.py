from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.main_menu_keyboard import start_keyboard
# from keyboards.keyboard_utils import game_keyboard
from lexicon.lexicon import LEXICON_RU


# init Router
router = Router()


# start handler
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=start_keyboard)


# help handler
@router.message(Command(commands="/help"))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


# any text message handler
@router.message()
async def plain_text(message: Message):
    await message.answer(
        text="Я умею только играть 🙃" \
        "Сыграем? -")