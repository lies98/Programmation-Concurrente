# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# exo1
from math import sqrt


def isocel(a, b, c):
    if (a == b and c <= a) or (a == c and b <= a) or (b == c and a <= c):
        return True
    else:
        return False


# exo2
def air_ordonne(a, b, c):
    somme = a + b + c
    u1 = min(a, b, c)
    u3 = max(a, b, c)
    u2 = somme - (u1 + u3)

    return 1 / 2 * sqrt(pow(u1, 2) * pow(u3, 2) - pow((pow(u1, 2) - pow(u2, 2) + pow(u3, 2)) / 2, 2))


def definit_triangle(a, b, c):
    return min(a, b, c) > 0 and max(a, b, c) < (a + b + c) / 2


def nb_triangles_speciaux(n, p):
    count = 0
    if p > n > 0:
        for a in range(n, p+1):
            for b in range(a+1, p+1):
                for c in range(b+1, p+1):
                    if definit_triangle(a, b, c) and air_ordonne(a, b, c) == (a + b + c):
                        print("a=", a, "b=", b, "c=", c)
                        count = count + 1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("--------------exo1--------------------------")
    # exo1 test
    print(isocel(4, 2, 3))
    print(isocel(2, 2, 20))
    print(isocel(20, 2, 2))
    print(isocel(2, 20, 2))
    print(isocel(2, 2, 2))
    print(isocel(2, 1, 2))
    print(isocel(2, 2, 1))
    print(isocel(1, 2, 2))

    print("--------------exo2--------------------------")
    # exo2_test
    print(air_ordonne(4, 2, 3))
    print(air_ordonne(4, 3, 3))
    print(air_ordonne(4, 4, 4))
    print(air_ordonne(3, 4, 5))
    print(air_ordonne(13, 14, 15))
    print(air_ordonne(1, 1, 1))

    print("--------------exo3--------------------------")

    print(definit_triangle(1, 1, 20))
    print(definit_triangle(4, 2, 3))
    print(definit_triangle(4, 4, 4))

    print("--------------exo4--------------------------")

    print(nb_triangles_speciaux(1, 20))
