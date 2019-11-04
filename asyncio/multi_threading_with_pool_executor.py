import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
'''
Other than handpicking a group of threads to execute and waiting using jon,
we can use threadpoolexecutor to dispatch threads. threadpoolexecutor will create a context on which these scheduled threads will execute and wait to complete through an implicit call to Join

The easiest way to create it is as a context manager, using the with statement to manage the creation and destruction of the pool.

The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. It then uses .map() 
to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.

The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool. It is strongly recommended
 that you use ThreadPoolExecutor as a context manager when you can so that you never forget to .join() the threads.

 Using sing a ThreadPoolExecutor can cause some confusing errors.

For example, if you call a function that takes no parameters, but you pass it parameters in .map(), the thread will throw an exception.

Unfortunately, ThreadPoolExecutor will hide that exception, and (in the case above) the program terminates with no output. This can be quite confusing to debug at first.
'''
def threading_func(tup):
    b, a = tup
    logging.info(f'Thred {a} is getting ready to sleep for {b} seconds')
    time.sleep(b)
    logging.info(f'Thred {a} finish executing')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt='%H:%M:%S')

    thread_parameter = []
    for i in range(5):
        thread_parameter.append((f'thread-{i}',i))
    
    try:
        with ThreadPoolExecutor(max_workers=4) as executor:
            fu = executor.map(threading_func,enumerate(thread_parameter))
            # for future in as_completed(fu):
            #     print(future)
    except Exception as ex:
        print(ex.args)
    else:
        print('With context waited for all threads to finish.')

   


