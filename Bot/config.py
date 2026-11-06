"""Bot configuration"""
import os

from dotenv import load_dotenv

load_dotenv()

class Configuration:
    TOKEN=os.getenv("TOKEN")
    OWNER_ID=os.getenv("OWNER_IDS")
    LOG_LEVEL=os.getenv("LOG_LEVEL")
    SYNC_ON_START = (
        os.getenv("SYNC_ON_START", "false").lower() == "true"
    )