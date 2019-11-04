#demo to access shared object using lock to avoid race condition
'''
A primitive lock is in one of two states, “locked” or “unlocked”.
It has two basic methods, acquire() and release(). 
When the state is unlocked, acquire() changes the state to locked and returns immediately. 
When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked,
then the acquire() call resets it to locked and returns.
The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately.
If an attempt is made to release an unlocked lock, a RuntimeError will be raised.

'''

import threading
import timer
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s')

class Counter(object):

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    
    def increment(self):
        logging.debug(f'Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Lock acquired')
            self.value += 1
        finally:
            logging.debug('Released lock')
            self.lock.release()
    
def worker(counter_instance):
    for i in range(2):
        r = random.random()
        logging.debug('Sleeping %0.02f',r)
        time.sleep(i)
        counter_instance.increment()
    logging.debug('Done')

if __name__ == "__main__":
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,)) #passing same instance as parameter to various thread and calling a increment method
        t.start()
    logging.debug('Waiting for worker threads')
    main_thread = threading.currentThread() #wait for all threads other than main before finishing
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d',counter.value)




