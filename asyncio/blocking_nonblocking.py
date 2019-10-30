import asyncio
import time

'''

blocking_call() calls the traditional time.sleep() internally,
which would have blocked the main thread and prevented your event loop from running.
This means that you must not make this function a coroutine, 
but even more severe, you cannot even call this function from anywhere in the main thread,
which is where the asyncio loop is running. We solve this problem by running this function in an executor.
'''
def blocking_call():
    print(f'{time.ctime()} from a thread!')
    time.sleep(0.5)
    print(f'{time.ctime()} hello from a thread!')

async def non_blocking_call():
    print(f'{time.ctime()} from non blocking coroutine')
    await time.sleep(1)
    print(f'{time.ctime()} hello from non blocking coroutine!')

e_loop = asyncio.get_event_loop()
task = asyncio.create_task(non_blocking_call())

'''
This is the last of our list of essential, must-know features of asyncio.
Sometimes you need to run things in a separate thread, oreven a separate process: this method is used for exactly that. Herewe pass our blocking function to be run in the default executor.5Note that run_in_executor() does not block the main thread: itonly schedules the executor task to run (it returns a Future, whichmeans you can await it if called within another coroutine function).The executor task will begin executing only once run_until_complete()is called, which allows the event loop to start processing events.
'''
e_loop.run_in_executor(None,blocking_call)