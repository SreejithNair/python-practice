# Custom logging

from os import path, makedirs # import from os to work with local path
from datetime import datetime #import datetime
from enum import Enum

class LogLevels(Enum):
    OFF     = 1
    MINIMUM = 2
    NORMAL  = 3
    DEBUG   = 4


class Logger(object):
    """Logger

    Logger class implement a custom logging which allow
    consumer to create log files under the directory from
    which it is executing.
    Based on the supplied file name, it create (if doesn't exists) a LogFiles directory
    and be ready to save files.
    """

    def __init__(self, full_name, log_level = LogLevels.DEBUG):
        module_name = path.splitext(path.basename(full_name))[0] # extract module name from .py file
        self.log_name = module_name + '.log'

        log_folder = 'Logfiles'
        if not path.exists(log_folder):
            makedirs(log_folder, exist_ok = True)
        
        self.log = path.join(log_folder, self.log_name)
        self.log_level = log_level

    def create_log(self, message = '', log_level = LogLevels.DEBUG):
        if self.log_level.value > log_level.value: #if passed in log level is less than instance level log then do not write log otherwise write log
            return

        with open(self.log, mode='w', encoding='utf-8') as log_file:
            #clean message
            msg = str(message)
            if msg.startswith('\n'):
                msg = msg[1:]
            #log_file.write(self.get_date_time()+'\t\t'+msg+)
            log_file.write(f'{self.get_date_time()}\t\t{msg}\n')
        log_file.close()
    
    def get_date_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')