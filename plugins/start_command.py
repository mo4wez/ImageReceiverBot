from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    chat_id = message.chat.id

    await client.send_message(
        chat_id=chat_id,
        text='Send me Image as a document:'
    )