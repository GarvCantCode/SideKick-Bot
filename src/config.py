"""Bot configuration"""

import os

from dotenv import load_dotenv

load_dotenv()

class Configuration:
    TOKEN=os.getenv("TOKEN")
    OWNER_ID=int(os.getenv("OWNER_ID"))
    LOG_LEVEL=os.getenv("LOG_LEVEL")
    SYNC_ON_START = (
        os.getenv("SYNC_ON_START", "false").lower() == "true"
    )