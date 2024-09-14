from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("oreo", "Вывести ооррео"),
            types.BotCommand("photo", "Фото леса"),
            types.BotCommand("random", "Рандомное 21323 число"),
            types.BotCommand("profile", "Ваш профиль"),
        ]
    )
