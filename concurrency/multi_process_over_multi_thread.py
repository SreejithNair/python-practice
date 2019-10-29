#If the GIL is causing you problems, here a few approaches you can try
'''
Multi-processing vs multi-threading: The most popular way is to use a multi-processing approach
where you use multiple processes instead of threads. Each Python process gets its own Python
interpreter and memory space so the GIL won’t be a problem. Python has a multiprocessing module
which lets us create processes
'''

from multiprocessing import Pool
import time

COUNT=50000000
def countdown(n):
    while

