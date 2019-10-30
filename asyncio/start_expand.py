import asyncio, time

async def do_sleep(seconds):
    print(f'do_sleep running loop:{asyncio.get_running_loop()}')
    await asyncio.sleep(seconds)

async def do_async():
    print(f'{time.ctime()} hello!')
    print(f'do_async running loop:{asyncio.get_running_loop()}')
    await do_sleep(2)
    print(f'I\'m up at {time.ctime()}.')

print(f'STA event loop{asyncio.get_event_loop()}')

#asyncio.run(do_async()) #this line is expanded below
event_loop = asyncio.get_event_loop() # get a loop to run the coroutine
task = event_loop.create_task(do_async()) # create task schedule the supplied coroutine to be run on that loop.
'''
The returned task object can be used to monitor the status of the task, 
for example whether it is still running or has completed, 
and can also be used to obtain a result value from your completed coroutine.
You can also cancel the task withtask.cancel()
'''
event_loop.run_until_complete(task) # block main thread until task (do_async()) coroutine complete.

'''
This call will block the current thread, which will usually be the main thread. 
Note that run_until_complete() will keep the loop running only until the given coro completes—
but all other tasks scheduled on the loop will also run while the loop is running. 
Internally, asyncio.run() calls run_until_complete() for you, 
and therefore blocks the main thread in the same way.
'''

pending = asyncio.all_tasks(loop=event_loop) #get all other coroutines running on that loop

for t in pending:
    t.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
event_loop.run_until_complete(group) # close all other coroutine running on that loop
'''
gather the still-pending tasks, cancel them, and then use loop.run_until_complete()
 again until those tasks are done.
 gather() is the method for doing the gathering.
 Note that asyncio.run() will do all of the cancelling, gathering, and waiting for pending tasks to finish up!
'''

event_loop.close()

'''
loop.close() is usually the final action: it must be called on a stopped loop,
and it will clear all queues and shut down the Executor.
 A “stopped” loop can be restarted, but a “closed” loop is gone for good.
 
 Internally,asyncio.run() will close the loop before returning. 
 This is fine because run() creates a new event loop every time you call it.
'''