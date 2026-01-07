import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(self.__class__.__name__)

        if not logger.handlers:
            fileHandler = logging.FileHandler("reports/logfile.log")
            formatter = logging.Formatter(
                "%(asctime)s :%(levelname)s :%(name)s :%(message)s"
            )
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

            logger.setLevel(logging.INFO)

        return logger

