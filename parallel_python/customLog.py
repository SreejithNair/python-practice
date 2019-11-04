import logging

LOG_FORMAT = '%(asctime)s %(threadname)-17s %(levelname)-8s %(message)s'

logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

def log(message):
    logging.debug(message)