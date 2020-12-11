from math import sqrt


def somme(vec):
    somme = 0
    for i in range(0, len(vec)):
        somme += vec[i]
    return somme


def moyenne(vec):
    return somme(vec) / len(vec)


def vec_soustrate_average(vec, avg):
    vec_out = []
    for i in range(0, len(vec)):
        vec_out.append(vec[i] - avg)
    return vec_out


def prod_vec(vec1, vec2):
    vec_out = []
    for i in range(0, len(vec1)):
        vec_out.append(vec1[i] * vec2[i])
    return vec_out


def ecartType(a, x):
    somme2 = 0
    for i in range(0, len(a)):
        somme2 += a[i] ** x
    return sqrt(somme2 / len(a))

def covarence(x,y):
    return somme(prod_vec(vec_soustrate_average(y, moyenne(y)), vec_soustrate_average(x, moyenne(x))))/len(x)

def calculR(x,y):
    return covarence(x,y)/(ecartType(vec_soustrate_average(x,moyenne(x)),2)*ecartType(vec_soustrate_average(y,moyenne(y)),2))

def equation_droite(x,y):
    a = covarence(x,y)/(ecartType(vec_soustrate_average(x,moyenne(x)),2)**2)
    b = moyenne(y) - a*moyenne(x)
    return [a,b]
if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    y = [49215, 35641, 45570, 53238, 36330, 40558, 58046, 60486, 86852, 38619, 20155, 20180, 35879, 33172, 23794, 32095,
         27228, 9406, 45522, 28383, 21150, 22882, 17881, 13157, 4452, 9155, 16282, 13563, 12459, 12580]
    y2 =[422,339,289,430,469,540,447,434,394,323,484,473,351,286,471,326,270,366,382,357,311,263,219,171,243,269,257,192,170,160]

    x_test = [2000,1500,1000,500,1000,1500,2000,2500]
    y_test = [0,3,6,10,8,5,2,-2]
    # print(vec_soustrate_average(y,moyenne(y)))
    # print(vec_soustrate_average(x,moyenne(x)))

    print(covarence(x,y))
    print(ecartType(vec_soustrate_average(x,moyenne(x)),2))
    print(ecartType(vec_soustrate_average(y,moyenne(y)),2))
    print(calculR(x,y))
    print(equation_droite(x,y))

    print(covarence(x,y2))
    print(ecartType(vec_soustrate_average(x,moyenne(x)),2))
    print(ecartType(vec_soustrate_average(y2,moyenne(y2)),2))
    print(calculR(x,y2))
    print(equation_droite(x, y2))

    print("-------------------------test---------------------")
    print(covarence(x_test,y_test))
    print(ecartType(vec_soustrate_average(x_test,moyenne(x_test)),2))
    print(ecartType(vec_soustrate_average(y_test,moyenne(y_test)),2))
    print(calculR(x_test,y_test))
    print(equation_droite(x_test, y_test))

    x3 = [i for i in range(1,24)]
    y3 = [33497,33170,32842,32345,31906,31197,31554,31481,30622,29972,29310,28648,28168,28313,28258,27639,27013,26703,26311,26070,26293,26365,25911]
    print(x3)

    print(covarence(x3,y3))
    print(ecartType(vec_soustrate_average(x3,moyenne(x3)),2))
    print(ecartType(vec_soustrate_average(y3,moyenne(y3)),2))
    print(calculR(x3,y3))
    print(equation_droite(x3,y3))
