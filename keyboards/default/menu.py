from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода"),
            KeyboardButton(text="Web камеры"),
            KeyboardButton(text="Еда"),
            KeyboardButton(text="Куда сходить?"),
        ],
    ],
    resize_keyboard=True
)
