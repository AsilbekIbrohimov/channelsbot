from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startkeyboard import startKeyboard
from loader import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name},\n\nElon yaratish uchun boshlash tugmasini bosing", reply_markup=startKeyboard)
    await state.finish()