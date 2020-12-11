from threading import Thread, RLock
from multiprocessing import Process, Lock
import sys
import time
import random

verrou = RLock()


def calcul_square(nombres):
    return [x ** 2 for x in nombres]


def calcul_cube(nombre):
    return [x ** 3 for x in nombre]


class exec(Thread):

    def __init__(self, nombres, calcul_type):
        Thread.__init__(self)
        self.nombres = nombres
        self.calcul_type = calcul_type

    def run(self):
        i = 0
        while i < 5:
            with verrou:
                if self.calcul_type == "square":
                    for nombre in calcul_square(self.nombres):
                        sys.stdout.write(str(nombre))
                        sys.stdout.flush()
                        attente = 0.2
                        attente += random.randint(1, 60) / 100
                        time.sleep(attente)
                elif self.calcul_type == "cube":
                    for nombre in calcul_cube(self.nombres):
                        sys.stdout.write(str(nombre))
                        sys.stdout.flush()
                        attente = 0.2
                        attente += random.randint(1, 60) / 100
                        time.sleep(attente)
                else:
                    print("this operation is not available")

            i += 1


def task(nombres, lock, calcul_type):
    lock.acquire()
    try:
        i = 0
        while i < 5:
            if calcul_type == "square":
                for nombre in calcul_square(nombres):
                    sys.stdout.write(str(nombre))
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            elif calcul_type == "cube":
                for nombre in calcul_cube(nombres):
                    sys.stdout.write(str(nombre))
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            else :
                print("this operation is not available")
            i += 1
    finally:
        lock.release()


if __name__ == '__main__':

    lock = Lock()
    nombres = [2, 3, 8, 9, 12]
    thread_1 = exec(nombres, "square")
    thread_2 = exec(nombres, "cube")

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print()

    procs = []
    proc1 = Process(target=task, args=(nombres, lock, "square"))
    proc2 = Process(target=task, args=(nombres, lock, "cube"))
    procs.append(proc1)
    procs.append(proc2)
    proc1.start()
    proc2.start()

    for proc in procs:
        proc.join()
