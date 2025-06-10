from typing import Any
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Filter
from keyboards.main_menu_keyboard import start_keyboard
from keyboards.keyboard_utils import game_keyboard
from lexicon.lexicon import LEXICON_RU
from services import services
from states import user_states


# init Router
router = Router()


# start handler
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=start_keyboard
    )


# help handler
@router.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# decline of game handler
@router.message(lambda message: message.text == "Не хочу!")
async def decline_game(message: Message):
    await message.answer(text=LEXICON_RU['decline_game'])


# start of game handler
@router.message(lambda message: message.text == "Давай!")
async def start_game(message: Message):
    await message.answer(
        text=LEXICON_RU['start_game'],
        reply_markup=game_keyboard
    )
    if not user_states.is_in_game(message.from_user.id):
        user_states.start_game(message.from_user.id)
    

@router.message.filter()
