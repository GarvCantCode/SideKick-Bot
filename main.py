"""Run the whole bot"""

from src.bot import core
from src.config import Configuration
from src.logger import setup_logging


def main():
    settings = {
        "token": Configuration.TOKEN,
        "owner_id": Configuration.OWNER_ID,
        "log_level": Configuration.LOG_LEVEL,
        "sync_on_start": Configuration.SYNC_ON_START,
    }

    logger = setup_logging(Configuration.LOG_LEVEL)
    bot = core(settings, logger)

    bot.run(Configuration.TOKEN, log_handler=None)

if __name__ == "__main__":
    main()