from  threading import Thread
from queue import Queue
import time

class Produce(Thread):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q
    def run(self):
        for i in range(1, 10):
            bz = self.name + ":" + str(i)
            self.q.put(bz)
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q
    def run(self):
        while True:
            try:
                bz = self.q.get(timeout = 3)
                print(self.name,"吃",bz)
                time.sleep(1)
            except:
                break
if __name__ == '__main__':
    q = Queue()
    bz_maker = ["生产者A","生产者B"]
    bz_eater = ["消费者1","消费者2","消费者3"]
    for maker in bz_maker:
        t = Produce(maker,q)
        t.start()
    for eater in bz_eater:
        t = Consumer(eater,q)
        t.start()