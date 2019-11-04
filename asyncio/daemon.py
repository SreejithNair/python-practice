import logging
import threading
import time

'''
setting daemon flag on a thread change the standard thread into daemon thread or background thread.
doing so, the main thread won't wait for daemon thread to complete before it exit. Call Join() otherwise to wait for all daemon thread to finish executing
'''

def threading_func(name,sleep):
    logging.info(f'Thred {name} is getting ready to sleep for {sleep} seconds')
    time.sleep(sleep)
    logging.info(f'Thred {name} finish executing')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt='%H:%M:%S')

    t = threading.Thread(target=threading_func,args=['thread-P',3],daemon=True)
    logging.info(f'thread is about to start')
    t.start()
    logging.info(f'finish executing main program')
    
    #following will make sure main thread will wait for all daemon to finish executing before exiting
    t.join()
    logging.info(f'all done')



