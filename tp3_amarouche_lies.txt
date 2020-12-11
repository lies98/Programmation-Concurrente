import time


def count_mot(phrase):
    cpt = 0
    phrase = phrase.strip()
    for index in range(len(phrase)):
        if phrase[index] == ' ' and phrase[index - 1] != ' ':
            cpt += 1
    return cpt + 1


def count_mot2(phrase):
    mots = [item for item in phrase.split() if item != " "]
    return len(mots)


def replace_multiple(s1, s2, n):
    s3 = list(s1)
    for index in range(n, len(s1), n):
        if len(s2) != 0:
            s3[index] = s2[0]
            s2 = s2.replace(s2[0], '', 1)

    return ''.join(s3) + s2


def termeU(n):
    if n == 0:
        return 1
    else:
        return termeU(n - 1) * 2 ** n + n


def series(n):
    res = 0;
    for i in range(0, n + 1):
        res += termeU(i)
    return res


def series_v2(n):
    res = [1]
    for i in range(1, n + 1):
        res.append(res[i - 1] * 2 ** i + i)
    return sum(res)
#pour le tableau pour n = 5
#res=[1]
#i:1 res=[1,3]
#i:2 res=[1,3,14]
#i:3 res=[1,3,14,115]
#i:4 res=[1,3,14,115,1844]
#i:5 res=[1,3,14,115,1844,59013]



def facto(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    print("count_mot(     hi hello     in the woods   ) ", count_mot("     hi hello     in the woods   "))
    print("count_mot2(     hi hello     in the woods   ) ", count_mot2("     hi hello     in the woods   "))
    print("replace_multiple(hirondelles, nid, 3) ", replace_multiple("hirondelles", "nid", 3))
    print("replace_multiple(abacus, oiseau, 2) ", replace_multiple("abacus", "oiseau", 2))
    print("replace_multiple( , , 2) ", replace_multiple("", "", 2))
    print("termeU(0) = ", termeU(0))
    print("termeU(1) = ", termeU(1))
    print("termeU(5) = ", termeU(5))
    print("termeU(10) = ", termeU(10))
    print("series(0) = ", series(0))
    print("series(1) = ", series(1))
    print("series(5) = ", series(5))
    print("series_v2(0) = ",series_v2(0))
    print("series_v2(1) = ",series_v2(1))
    print("series_v2(5) = ",series_v2(5))

    depart = time.clock()
    series(100)
    arrive = time.clock()
    print("series(100) met ", arrive - depart)

    depart = time.clock()
    series_v2(100)
    arrive = time.clock()
    print("series_v2(100) met ", arrive - depart)

    depart = time.clock()
    series(300)
    arrive = time.clock()
    print("series(300) met ", arrive - depart)

    depart = time.clock()
    series_v2(300)
    arrive = time.clock()
    print("series_v2(300) met ", arrive - depart)

    depart = time.clock()
    series(400)
    arrive = time.clock()
    print("series(400) met ", arrive - depart)

    depart = time.clock()
    series_v2(400)
    arrive = time.clock()
    print("series_v2(400) met ", arrive - depart)

    depart = time.clock()
    series_v2(1000)
    arrive = time.clock()
    print("series_v2(1000) met ", arrive - depart)

    print("on remarque que seriesV2 est bien plus puissant que series")

    print("facrtorielle(1) = ", facto(1))
    print("facrtorielle(2) = ", facto(2))
    print("facrtorielle(3) = ", facto(3))
    print("facrtorielle(4) = ", facto(4))
