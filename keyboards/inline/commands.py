from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(text="Орео", callback_data="oreo"), InlineKeyboardButton(text="Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="Фото", callback_data="photo"), InlineKeyboardButton(text="Уведомление", callback_data="alarm")],
    [InlineKeyboardButton(text="Рандомное число", callback_data="RandomNum")]
])