from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

submitKeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ha'),      
        ]
    ],
    resize_keyboard=True
)