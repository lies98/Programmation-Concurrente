from multiprocessing import Process, Lock, Queue
import time
import sys
import random


# def print_func(continent='Asia'):
#     print("the name of continent is : ", continent)
#
#
#
#
# if __name__ == '__main__':
#     names = ['America', 'Europa', 'Africa']
#     procs = []
#     proc = Process(target=print_func())
#     procs.append(proc)
#     proc.start()
#
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()

# colors = ["red", "green", "bleu", "black"]
# cnt = 1
#
# queue = Queue()
# print("pushing items into queue")
#
# for color in colors:
#     print("item nb ", cnt, " ", color)
#     queue.put(color)
#     cnt += 1
# print('\npoping items from queue:')
#
# cnt = 0
#
# while not queue.empty():
#     print('items no: ', cnt, " ", queue.get())
#     cnt += 1

# def task(mot):
#     i = 0
#     while i < 5:
#         with verrou:
#             for letter in mot:
#                 sys.stdout.write(letter)
#                 sys.stdout.flush()
#                 attente = 0.2
#                 attente += random.randint(1, 60) / 100
#                 time.sleep(attente)
#
#         i += 1
def task(mot, lock):
    lock.acquire()
    try:
        i = 0
        while i < 5:
            for letter in mot:
                sys.stdout.write(letter)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
            i += 1
    finally:
        lock.release()


def main():
    """main programme"""
    lock = Lock()
    colors = ["red", "green", "bleu", "black"]
    procs = []
    for color in colors:
        proc = Process(target=task, args=(color, lock))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    main()
