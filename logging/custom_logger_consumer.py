from custom_logging import Logger, LogLevels
from os import path

if __name__ == '__main__':
    
    logger = Logger(__file__)                       #__file__ is the full name of current python module
    
    #Just to double check whether we are writing entry under the same folder from where this
    #consumer object is consuming

    print(__file__)
    print(path.basename(__file__))
    print(logger.log_name)

    #start placing loggs
    logger.create_log('regular log message')
    logger.create_log('\nOther log message')
    logger.create_log('\Last log message')

    logger.create_log('\Level log message',log_level=LogLevels.OFF)

    logger_second = Logger(__file__,LogLevels.MINIMUM) # this instance would only allow you to write log more than MINIMUM level
    logger_second.create_log("Debug log") # this won't log
    logger_second.create_log("DEBUG log",LogLevels.DEBUG) # this will log


