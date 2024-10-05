from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startKeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Boshlash'),      
        ]
    ],
    resize_keyboard=True
)