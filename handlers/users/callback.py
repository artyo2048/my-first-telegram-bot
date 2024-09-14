import random

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.commands import menu
from loader import dp


@dp.callback_query_handler(Text(equals="profile"))
async def show_profile(call:types.CallbackQuery):
    await call.message.answer('Ваш профиль:\n'
                         f'Имя пользователя: {call.from_user.username}\n'
                         f'Имя: {call.from_user.first_name}')

@dp.callback_query_handler(Text(equals="alarm"))
async def alarm(call:types.CallbackQuery):
    await call.answer('АЛАРМААА!', show_alert=True)

@dp.callback_query_handler(Text(equals="RandomNum"))
async def random_num(call:types.CallbackQuery):
    await call.answer(str(random.randint(1,50000)))

@dp.callback_query_handler(Text(equals="oreo"))
async def random_num(call:types.CallbackQuery):
    await call.message.answer('<b> орео </b>' '<i> орео </i>''<a href="https://ru.wikipedia.org/wiki/Oreo"> орео </a>')

@dp.callback_query_handler(Text(equals="photo"))
async def random_num(call:types.CallbackQuery):
    url = 'https://31.vtorproekt.com/upload/iblock/08d/w71mv8770qkmc3ep5dkfwhi257y5qy8r.jpg'
    await call.message.answer_photo(
        photo=url,
        caption="Лес..."
    )

