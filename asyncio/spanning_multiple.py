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

    threads = list()
    for i in range(5):
        logging.info(f'thread-{i} created.')
        threads.append(threading.Thread(target=threading_func,args=[f'thread-{i}',i]))
        threads[-1].start()
    
    for index,thread in enumerate(threads):
        logging.info(f'main:before joining thread {index}')
        thread.join()
        logging.info(f'main: thread {index} done')
    


