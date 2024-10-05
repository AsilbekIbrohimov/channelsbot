from aiogram.dispatcher.filters.state import StatesGroup, State

class info(StatesGroup):
    channel_name = State()
    username = State()
    admin = State()
    language = State()
    sub = State()
    price = State()
    period = State()
    more = State()
    logo = State()
    ha = State()