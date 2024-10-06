from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.infostate import info
from aiogram.types import Message, ReplyKeyboardRemove
from data.config import ADMINS
from handlers.users.start import bot_start
from aiogram.types import ContentType
from keyboards.default.submitkeyboard import submitKeyboard

@dp.message_handler(text = 'Boshlash')#, commands='boshlash')
async def Izlash(message: types.Message, state: FSMContext):
        await message.answer("Hozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.", reply_markup=ReplyKeyboardRemove())
        await message.answer("Kanal nomini kiriting")
        await info.channel_name.set()
@dp.message_handler(state=info.channel_name)
async def answer_channelname(message: types.Message, state: FSMContext):
        channelname = message.text
        await state.update_data(
                {
                        'name': channelname,
                }
        )
        await message.answer("username")
        await info.next()


@dp.message_handler(state=info.username)
async def answer_channelname(message: types.Message, state: FSMContext):
        username = message.text
        await state.update_data(
                {
                        'username': username,
                }
        )
        await message.answer("Admin kontaktini kiriting")
        await info.next()
@dp.message_handler(state=info.admin)
async def answer_channelname(message: types.Message, state: FSMContext):
        admin = message.text
        await state.update_data(
                {
                        'admin': admin,
                }
        )
        await message.answer("Kanal tili")
        await info.next()

@dp.message_handler(state=info.language)
async def answer_channelname(message: types.Message, state: FSMContext):
        language = message.text
        await state.update_data(
                {
                        'language': language,
                }
        )
        await message.answer("Reklama narxlarini kiritng")
        await info.next()
@dp.message_handler(state=info.sub)
async def answer_channelname(message: types.Message, state: FSMContext):
        sub = message.text
        await state.update_data(
                {
                        'sub': sub,
                }
        )
        await message.answer("Obunachilar soni:")
        await info.next()
@dp.message_handler(state=info.price)
async def answer_channelname(message: types.Message, state: FSMContext):
        price = message.text
        await state.update_data(
                {
                        'price': price,
                }
        )
        await message.answer("Murojat qilish vaqti")
        await info.next()
@dp.message_handler(state=info.period)
async def answer_channelname(message: types.Message, state: FSMContext):
        period = message.text
        await state.update_data(
                {
                        'period': period,
                }
        )
        await message.answer("Ko'proq malumot qoldiring")
        await info.next()

@dp.message_handler(state=info.more)
async def answer_channelname(message: types.Message, state: FSMContext):
        more = message.text
        await state.update_data(
                {
                        'more': more,
                }
        )
        await message.answer("logotip yuboring")
        await info.next()

@dp.message_handler(content_types=ContentType.PHOTO ,state=info.logo)
async def answer_channelname(message: types.Message, state: FSMContext):
        logo = message.photo[-1].file_id
        await state.update_data(
                {
                        'logo': logo
                }
        )
        
        data = await state.get_data()
        channelname = data.get("name")
        username = data.get("username")
        admin = data.get("admin")
        language = data.get('language')
        sub = data.get('sub')
        price = data.get('price')
        period = data.get('period')
        more = data.get('more')
        logo = data.get('logo')

        msg = "Telegram kanal\n"
        msg += f"✏️ Nomi: {channelname}\n"
        msg += f"🇺🇿 Telegram: {username}\n"
        msg += f"👨🏻‍💻 Admin: {admin}\n"
        msg += f"🌐 Til: {language}\n"
        msg += f"👥 Obunachilar soni: {sub}\n"
        msg += f"💰 Reklama narxi: {price}\n"
        msg += f"🕰 Murojaat qilish vaqti: {period}\n"
        msg += f"🔎 Batafsil: {more}\n"
        await message.answer_photo(logo, caption=msg, reply_markup=submitKeyboard)
        await message.answer("Malumotlar togriligini tasdiqlaysizmi")

        await info.next()
@dp.message_handler(content_types=ContentType.ANY ,state=info.logo)
async def answer_channelname(message: types.Message, state: FSMContext):
       await message.answer("Rasm yuboring")

@dp.message_handler(state=info.ha)
async def answer_channelname(message: types.Message, state: FSMContext):
    if message.text == "Ha": 
        data = await state.get_data()
        channelname = data.get("name")
        username = data.get("username")
        admin = data.get("admin")
        language = data.get('language')
        price = data.get('price')
        period = data.get('period')
        more = data.get('more')
        logo = data.get('logo')

        msg = "Telegram kanal\n"
        msg += f"✏️ Nomi: {channelname}\n"
        msg += f"🇺🇿 Telegram: {username}\n"
        msg += f"👨🏻‍💻 Admin: {admin}\n"
        msg += f"🌐 Til: {language}\n"
        msg += f"💰 Reklama narxi: {price}\n"
        msg += f"🕰 Murojaat qilish vaqti: {period}\n"
        msg += f"🔎 Batafsil: {more}\n"
        await message.answer('Adminga yuborildi', reply_markup=ReplyKeyboardRemove())
        for admin in ADMINS:
            await bot.send_photo(photo=logo, caption=msg, chat_id=admin)
        # State dan chiqaramiz
        # 1-variant
        await state.finish()
        await bot_start(message, state)
    else:
           pass