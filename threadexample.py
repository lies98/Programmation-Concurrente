import random
import sys
from threading import Thread, RLock
import time

verrou = RLock()


# class Afficheur(Thread):
#     def __init__(self, letter):
#         Thread.__init__(self)
#         self.letter = letter
#
#     def run(self):
#         i = 0
#         while i < 20:
#             sys.stdout.write(self.letter)
#             sys.stdout.flush()
#             attente = 0.2
#             attente += random.randint(1, 60) / 100
#             time.sleep(attente)
#             i += 1

# class Afficheur(Thread):
#     def __init__(self, mot):
#         Thread.__init__(self)
#         self.mot = mot
#
#     def run(self):
#         i = 0
#         while i < 5:
#             for letter in self.mot:
#                 sys.stdout.write(letter)
#                 sys.stdout.flush()
#                 attente = 0.2
#                 attente += random.randint(1, 60) / 100
#                 time.sleep(attente)
#             i += 1

class Afficheur(Thread):
    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        i = 0
        while i < 5:
            with verrou:
                for letter in self.mot:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)

            i += 1


if __name__ == '__main__':
    thread_1 = Afficheur("canard")
    thread_2 = Afficheur("TORTUE")

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
