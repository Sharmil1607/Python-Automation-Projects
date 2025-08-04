import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger("automationLogger")  # Named logger

        if not logger.handlers:  # Avoid adding handlers multiple times
            logger.setLevel(logging.INFO)

            log_dir = ".\\Logs"
            os.makedirs(log_dir, exist_ok=True)  # Create Logs dir if not exists

            file_handler = logging.FileHandler(os.path.join(log_dir, "automation.log"), mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I%M%S %p')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger
