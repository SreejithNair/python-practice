#https://docs.python.org/3.3/library/logging.html
import logging

#if following configuration is not specified we would be logging under root level.
# here we need to log at file level. so following __main__ will do the trick
log=logging.getLogger(__name__)
#Keep logging format since we are not changing this
FORMAT = '%(asctime)s:\t%(name)s:\t%(levelname)s:\t%(message)s'
logging.basicConfig(filename='logging\\application.log',
                    level=logging.DEBUG,
                    format=FORMAT)


log.debug('This is a debug message')
log.info('This is a info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.critical('This is a critical message')

'''
Simple multi line comment
2019-10-04 22:17:22,834:	root:	DEBUG:	This is a debug message
2019-10-04 22:17:22,834:	root:	INFO:	This is a info message
2019-10-04 22:17:22,834:	root:	WARNING:	This is a warning message
2019-10-04 22:17:22,835:	root:	ERROR:	This is an error message
2019-10-04 22:17:22,835:	root:	CRITICAL:	This is a critical message

log=logging.getLogger(__name__)

2019-10-04 22:25:46,579:	__main__:	DEBUG:	This is a debug message
2019-10-04 22:25:46,580:	__main__:	INFO:	This is a info message
2019-10-04 22:25:46,580:	__main__:	WARNING:	This is a warning message
2019-10-04 22:25:46,580:	__main__:	ERROR:	This is an error message
2019-10-04 22:25:46,581:	__main__:	CRITICAL:	This is a critical message
'''