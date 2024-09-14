import random

from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp


@dp.message_handler(Command("random"))
async def randomC(message: types.Message):
    await message.answer(str(random.randint(1,50000)))