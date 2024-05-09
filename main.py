from pyrogram import Client
from bot_config import BotConfig
import pyromod
import logging

# configure plugins
plugins = dict(root="plugins")

# read .env file
config = BotConfig()

api_id = config.api_id
api_hash = config.api_hash
token = config.token

# Client instance
bot = Client(
    name="ImageBot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
    plugins=plugins,
)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot.run()