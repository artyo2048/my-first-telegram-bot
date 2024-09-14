from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.commands import menu
from loader import dp


@dp.message_handler(Command("help"))
async def helpC(message: types.Message):
    await message.answer("Наши команды: ",reply_markup=menu)
