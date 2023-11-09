import logging

class GenerateLogger:
    @staticmethod
    def gen_logs():
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(".\\Logs\\NopCommerce_Logs.log")
        file_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s %(message)s",datefmt="%d/%m/%Y %I:%M:%S")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger