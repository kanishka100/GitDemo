import inspect
import logging

import pytest


@pytest.mark.usefixtures('setup')
class Base_Class:
    def get_logger(self):
        # this is how you get the name of the file who called the method
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter_obj = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s %(message)s")
        file_handler.setFormatter(formatter_obj)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger
