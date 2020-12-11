import time
import random
from multiprocessing import Process, Queue


def wait():
    attente = 0.2
    attente += random.randint(1, 60) / 100
    time.sleep(attente)


class Producteurs(Process):

    def __init__(self, queue, number):
        Process.__init__(self)
        self.queue = queue
        self.number = number

    def run(self):
        while True:
            if not self.queue.full():
                item = random.randint(1, 100)
                self.queue.put(item)
                print(f"\033[94mPutting {item} in producer {self.number} \033[0m")
                wait()


class Consumers(Process):

    def __init__(self, queue, number):
        Process.__init__(self)
        self.queue = queue
        self.number = number
        return

    def run(self):
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                print(f"\033[91mgetting {item} in consumer {self.number} \033[0m")
                wait()


if __name__ == '__main__':


    producers = []
    consumers = []
    queue = Queue()
    prod_nb = int(input("veuillez renter le nombre de producteurs : "))
    cons_nb = int(input("veuillez renter le nombre de consomateur : "))
    queue_size = int(input("veuillez la taille de la file,Tapez Zero pour une taille infinie : " ))
    if queue_size > 0:
        queue = Queue(queue_size)

    for n in range(1,prod_nb+1):
        producers.append(Producteurs(queue, n))

    for n in range(1, cons_nb+1):
        consumers.append(Consumers(queue, n))

    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
