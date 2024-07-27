from loguru import logger


def greet():
    logger.info("Called greet")
    print("Hey there!")
