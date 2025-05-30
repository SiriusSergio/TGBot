from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (KeyboardButton,
                           ReplyKeyboardMarkup)

# initializing builder for keyboards
kb_builder = ReplyKeyboardBuilder()

# button to start the game
confirm_button = KeyboardButton(text='Давай!')

# reject button
reject_button = KeyboardButton(text='Не хочу!')

# adding buttons in builder
kb_builder.row(
    confirm_button,
    reject_button
)

# creating keyboard
start_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Используй кнопки"
)
