from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def get_file_id(message: types.Message):
    if message.photo:
        photo_file_id = message.photo[-1].file_id
        await message.reply(f'File_ID этой фотографии: \n'
                            f'<code>{photo_file_id}</code>')
    elif message.video:
        video_file_id = message.video.file_id
        await message.reply(f'File_ID этого видео: \n'
                                f'<code>{video_file_id}</code>')
    elif message.voice:
        voice_file_id = message.voice.file_id
        await message.reply(f'File_ID этого гс: \n'
                                f'<code>{voice_file_id}</code>')
    elif message.video_note:
        vn_file_id = message.video_note.file_id
        await message.reply(f'File_ID этого кружка: \n'
                                f'<code>{vn_file_id}</code>')
    elif message.document:
        doc_file_id = message.document.file_id
        await message.reply(f'File_ID этого документа: \n'
                                f'<code>{doc_file_id}</code>')
    elif message.sticker:
        sticker_file_id = message.sticker.file_id
        await message.reply(f'File_ID этого стикера: \n'
                                f'<code>{sticker_file_id}</code>')
