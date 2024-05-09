from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

# List of categories
CATEGORIES = [
    "Urban Damage",
    "Traffic Sign",
    "Selfie",
    "Pet",
    "Park",
    "Accidents",
    "Natural Disaster",
    "Food"
]

# Create reply keyboard markup
category_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton(category)] for category in CATEGORIES
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)