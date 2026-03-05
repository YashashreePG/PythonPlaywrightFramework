import logging
import os
from datetime import datetime


class Logger:

    @staticmethod
    def get_logger():

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        # Create logs folder
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        # Log file name with timestamp
        log_file = os.path.join(
            log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        # File handler
        file_handler = logging.FileHandler(log_file)

        # Console handler
        console_handler = logging.StreamHandler()

        # Log format
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger