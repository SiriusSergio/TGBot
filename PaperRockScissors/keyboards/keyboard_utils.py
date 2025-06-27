from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU


# initializing builder for keyboards
kb_builder = ReplyKeyboardBuilder()

# button to form rock
rock_button = KeyboardButton(text=LEXICON_RU["rock"])

# button to form paper
paper_button = KeyboardButton(text=LEXICON_RU["paper"])

# button to form scissors
scissort_button = KeyboardButton(text=LEXICON_RU["scissors"])

kb_builder.row(rock_button, paper_button, scissort_button, width=1)

game_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True, one_time_keyboard=False
)
