import os
import json
from pathlib import Path
from dotenv import load_dotenv
from exceptions import InvalidJsonConfigFileException


class BotConfig:
    def __init__(self):
        try:
            self.token, self.api_hash, self.api_id = self._read_env_config()
        except InvalidJsonConfigFileException:
            exit(2)

    def _read_env_config(self):
        load_dotenv(verbose=False)
        env_path = Path('./env') / '.env'
        load_dotenv(dotenv_path=str(env_path))

        token = os.getenv("TOKEN")
        api_hash = os.getenv("API_HASH")
        api_id = os.getenv("API_ID")
        
        return token, api_hash, api_id

