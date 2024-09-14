import random

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.commands import menu
from loader import dp


@dp.message_handler(Text(equals="Помощь❔"))
async def helpC(message: types.Message):
    await message.answer("Наши команды: ",reply_markup=menu)