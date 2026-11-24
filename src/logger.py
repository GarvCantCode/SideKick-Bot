"""Bot logger shows the logs in modes: Error, Debug, Info, Warning, Critical"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOGGER_NAME = "sidekick"
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class ColorFormatter(logging.Formatter):
    RESET = "\x1b[0m"
    GRAY = "\x1b[90m"
    GREEN = "\x1b[32m"
    
    LEVEL_COLORS = {
        logging.DEBUG: "\x1b[37m",
        logging.INFO: "\x1b[34m",
        logging.WARNING: "\x1b[33m",
        logging.ERROR: "\x1b[31m",
        logging.CRITICAL: "\x1b[1;31m",
    }
    
    def __init__(self):
        super().__init__()
        self._formatters = {}
        
        for level, color in self.LEVEL_COLORS.items():
            fmt = (
                f"{self.GRAY}{{asctime}}{self.RESET} "
                f"{color}{{levelname:<8}}{self.RESET} "
                f"{self.GREEN}{{name}}{self.RESET} {{message}}"
            )
            self._formatters[level] = logging.Formatter(fmt, DATE_FORMAT, style="{")

    def format(self, record):
        formatter = self._formatters.get(record.levelno, self._formatters[logging.INFO])
        return formatter.format(record)
    
def setup_logging(level=None):
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

    level_name = (level or "INFO").upper()
    numeric_level = logging.getLevelNamesMapping().get(level_name, logging.INFO)

    console = logging.StreamHandler()
    console.setFormatter(ColorFormatter())

    LOG_DIR.mkdir(exist_ok=True)
    file_handler = RotatingFileHandler(
        LOG_DIR / "sidekick.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(
        logging.Formatter(
            "[{asctime}] [{levelname:<8}] {name}: {message}", DATE_FORMAT, style="{"
        )
    )

    logger.setLevel(numeric_level)
    logger.addHandler(console)
    logger.addHandler(file_handler)
    logger.propagate = False
    
    discord_logger = logging.getLogger("discord")
    discord_logger.setLevel(max(numeric_level, logging.INFO))
    discord_logger.addHandler(console)
    discord_logger.addHandler(file_handler)
    discord_logger.propagate = False
    
    return logger