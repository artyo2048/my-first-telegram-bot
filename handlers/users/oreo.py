from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp


@dp.message_handler(Command("oreo"))
async def oreoC(message: types.Message):
    await message.answer('<b> орео </b>' '<i> орео </i>''<a href="https://ru.wikipedia.org/wiki/Oreo"> орео </a>')
