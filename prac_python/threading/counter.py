import time
from threading import Thread


class Counter(Thread):
    def __init__(self, init_=0, offset=1):
        super(Counter, self).__init__()
        self.counter = init_
        self.offset = offset
        self.shutting_down = False

    def increment(self):
        self.counter = self.counter + self.offset

    def print_ctr(self):
        print('Counter: %s' % self.counter)

    def run(self):
        while True:
            while not self.shutting_down:
                self.increment()
                self.print_ctr()
                time.sleep(1)

    def shutdown(self):
        self.shutting_down = True

    def start_thread(self):
        self.shutting_down = False


if __name__ == '__main__':
    counter = Counter(5, 5)
    counter.start()
    time.sleep(10)
    counter.shutdown()
    time.sleep(2)
    counter.start_thread()

