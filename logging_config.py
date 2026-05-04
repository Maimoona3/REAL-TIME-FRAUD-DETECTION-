import logging
from logging.handlers import RotatingFileHandler


def setup_logging():

    logger = logging.getLogger("fraud_logger")

    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        "fraud_system.log",
        maxBytes=1000000,
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger