#here due to GIL both STA and MTA version perform more or less same.
import time
from threading import Thread

COUNT = 50000000
def countdown(n):
    while n>=0:
        n-=1

starttime=time.time()
countdown(COUNT)
end=time.time()
print(f'Time elapsed(STA):{end-starttime}')

print(f'Using threads')

t1 = Thread(target=countdown,args=(COUNT//2,))
t2 = Thread(target=countdown,args=(COUNT//2,))

starttime=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f'Time elapsed (Multiple):{end-starttime}')

# both versions take almost same amount of time to finish.
# In the multi-threaded version the GIL prevented the CPU-bound threads from executing in parellel.
# The GIL does not have much impact on the performance of I/O-bound multi-threaded programs
# as the lock is shared between threads while they are waiting for I/O. 


