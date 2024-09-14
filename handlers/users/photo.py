from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("photo"))
async def photoC(message: types.Message):
    url = 'https://31.vtorproekt.com/upload/iblock/08d/w71mv8770qkmc3ep5dkfwhi257y5qy8r.jpg'
    await message.answer_photo(
        photo=url,
        caption="Лес..."
    )