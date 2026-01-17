import os
import sys
from loguru import logger

log_level = os.getenv("LOG_LEVEL", "DEBUG")
logger.add(
    sys.stdout, format="{time} {level} {message}", filter="my_module", level=log_level
)

logger.add("logs/app.log", serialize=True, rotation="10 MB")

logger.level(log_level)
