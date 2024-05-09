import os
from pyrogram import Client, filters
from pyrogram.types import Message
from constants.keyboards import category_keyboard

# Directory to save the photos
SAVE_DIRECTORY = "saved_photos"

# Ensure the directory exists, if not, create it
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

@Client.on_message(filters.document)
async def get_image(client: Client, message: Message):
    chat_id = message.chat.id

    # Ensure the document is a photo
    document = message.document
    if document.mime_type != "image/jpeg" and document.mime_type != "image/png":
        return
    
    # Get the file ID
    file_id = document.file_id

    # Ask the user to choose a category
    await message.reply_text("Please choose a category for this photo:", reply_markup=category_keyboard)

    # Wait for the user's response
    response = await client.listen(filters.text & filters.private)

    # Get the chosen category
    chosen_category = response.text

    # Download the photo
    file_path = await client.download_media(file_id)

    # Move the photo to the chosen category directory
    category_directory = os.path.join(SAVE_DIRECTORY, chosen_category)
    os.makedirs(category_directory, exist_ok=True)
    file_name = document.file_name
    save_path = os.path.join(category_directory, file_name)
    os.rename(file_path, save_path)

    # Send a confirmation message
    await response.reply_text(f"Photo saved in {chosen_category} category.")

