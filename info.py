import os
from dotenv import load_dotenv


load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION = os.getenv("SESSION", "")
DATABASE_URI = os.getenv("DATABASE_URI", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
ADMIN = int(os.getenv("ADMIN", ""))
CHANNEL = os.getenv("CHANNEL", "")
