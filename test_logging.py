import logging


def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # accepts filehandler object
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information message")
    logger.warning("Warning Message")
    logger.error("Major Failure")
    logger.critical("Critical Failure")
