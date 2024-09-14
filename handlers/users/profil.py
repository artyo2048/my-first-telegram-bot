from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp


@dp.message_handler(Command("profile"))
async def profileC(message: types.Message):
    await message.answer('Ваш профиль:\n'
                         f'Имя пользователя: {message.from_user.username}\n'
                         f'Имя: {message.from_user.first_name}')