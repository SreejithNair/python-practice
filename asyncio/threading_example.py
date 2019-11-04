import logging
import threading
import time

def threading_func(name,sleep):
    logging.info(f'Thred {name} is getting ready to sleep for {sleep} seconds')
    time.sleep(sleep)
    logging.info(f'Thred {name} finish executing')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt='%H:%M:%S')

    t = threading.Thread(target=threading_func,args=['thread-P',3])
    logging.info(f'thread is about to start')
    t.start()
    logging.info(f'waiting for thread to finish')
    #with following, main thread will wait for all threads to finish their execution before exiting the application
    logging.info(f'all done')

    #following will make sure main thread will wait for all threads before executing last logging line
    #t.join()
    #logging.info(f'all done')



