import logging
import sys

from constants import LOG_FORMAT, LOG_LEVEL


def configure_logger() -> None:
    formatter = logging.Formatter(LOG_FORMAT)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)
