import threading
import customLog
import time

items = []
condition = threading.Condition()

class Consumer(threading.Thread):

    def __init__(self):
        #super().__init__(self,args=args,kwargs=kwargs)
        threading.Thread.__init__(self)
    
    def consume(self):

        with condition:
            if len(items) == 0:
                customLog.log('No items to consume')
                condition.wait()

            while len(items) > 0:
                x = items.pop()
                customLog.log(f'Consumed item:{x}')

            condition.notify()

    def run(self):
        while True:
            self.consume()

class Producer(threading.Thread):

    def __init__(self):
        #super().__init__(self,args = args, kwargs = kwargs)
        threading.Thread.__init__(self)
    
    def produce(self):

        with condition:
            for i in range(5):
                customLog.log(f'Producer is adding item:{i}')
                items.append(f'Item :{i}')
            
            condition.notify()
    
    def run(self):
        while True:
            for i in range(5):
                time.sleep(i*0.5)
                self.produce()