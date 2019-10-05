import logging

log = logging.getLogger(__name__) #recommended to use __name__ to know the source of log
log.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:\t%(name)s:\t%(levelname)s:\t%(message)s' # format
formatter = logging.Formatter(FORMAT)
#compare handlers and formatter to basicConfig below

#log to an external file - all levels
file_handler = logging.FileHandler('logging\\log_a.log')
file_handler.setFormatter(formatter)

#log to console anything above warning
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING) #overriding DEBUG to WARNING only for console logging.
console_handler.setFormatter(formatter)

#now add these handler to logger
log.addHandler(file_handler)
log.addHandler(console_handler)


log.debug('This is a debug message')
log.info('This is a info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.critical('This is a critical message')