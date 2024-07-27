from loguru import logger
from custom_functions import greet

if __name__ == "__main__":
    greet()
    logger.success("Successfully terminated")
