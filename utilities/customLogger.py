import logging
import os

class LogHandler:

    @staticmethod
    def loggen():
        # Ensure the Logs directory exists
        log_dir = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create logger
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.INFO)

        # Create file handler
        file_handler = logging.FileHandler(os.path.join(log_dir, "automation.log"))
        file_handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s'))
        
        # Avoid adding duplicate handlers
        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger