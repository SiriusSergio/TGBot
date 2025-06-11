from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


# init Router
router = Router()


# any text message handler
@router.message()
async def plain_text(message: Message):
    await message.answer(text=LEXICON_RU["other_message"])
