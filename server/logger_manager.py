import logging

from . import config
from .config import OutputMode


class LoggerManager:
    output_mode = config.OUTPUT_MODE

    @staticmethod
    def configure_logger(logger, level):
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(level)
        logger.addHandler(handler)

    def get_logger(logger_name):
        logger = logging.getLogger(logger_name)
        if config.OUTPUT_MODE == OutputMode.DEBUG:
            LoggerManager.configure_logger(logger, logging.DEBUG)
        if config.OUTPUT_MODE == OutputMode.VERBOSE:
            LoggerManager.configure_logger(logger, logging.INFO)
        return logger
