"""Run the whole bot"""
from Bot.bot import core
from Bot.config import Configuration
from Bot.logger import setup_logging


def main():
    settings = {
        "token": Configuration.TOKEN,
        "owner_id": Configuration.OWNER_ID,
        "log_level": Configuration.LOG_LEVEL,
        "sync_on_start": Configuration.SYNC_ON_START,
    }

    logger = setup_logging(Configuration.LOG_LEVEL)
    bot = core(settings, logger)

    bot.run(Configuration.TOKEN)

if __name__ == "__main__":
    main()