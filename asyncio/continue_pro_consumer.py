import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()
            
            while len(items) > 0:
                x= items.pop()
                logging.info(f'Consuming: {x}')
            
            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(0.5)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 10:
                logging.info('Waiting for the queue to clear as there are 10 items to consume')
                condition.wait()

            for i in range(5):
                rand=random.randint(0,256)
                items.append(f'Item:{rand} in queue')
                logging.info(f'Adding {rand} to queue')

            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(0.5)
            self.produce()


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()