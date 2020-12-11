# part 3 introduction
import json
from collections import deque
import fibo
import math


def numbers():
    print("addtion 2 + 2 ", 2 + 2)
    print("soustraction et multiplcation avec respect des prioritées 50 - 5 * 6 = ", 50 - 5 * 6)
    print("le signe de la division / retourne un float (50 - 5 * 6) / 4 = ", (50 - 5 * 6) / 4)  # / always return float
    print("la division entiere avec // (50 - 5 * 6) // 4 = ", (50 - 5 * 6) // 4)  # // floor division
    print("le reste de la division avec % ", (50 - 5 * 6) % 4)  # % the remain
    print("la puissance avec ** : 5**2 = ", 5 ** 2)  # power with **
    width = 20  # affectation
    print("l'affectation avec = ", width)
    # print (height) return an error height undefined
    print("int * float = float", 4 * 3.75 - 1)  # int * float = float
    print("En mode interactif, la dernière expression affichée est affectée à la variable _")


def str():
    print("les chaines de caractères sont exprimées en guillemets simples ou entre doubles quotes ")
    print("l\'affectation marche aussi avec les chaines de caracteres ")
    print(r'path\user\desktop' + " ceci est un exemple de raw string pour ne pas interpreter les caracteres speciauxx")
    print("""avec les triples quotes les retours 
    a la ligne sont
    inclus """)
    print("concatenation avec le symbole + et et 3 * myString affiche ", 3 * "myString")
    print(
        "Plusieurs chaînes de caractères " "ecrites cote a cote " "sont automatiquement concaténées" " comme dans cet exemple")
    word = "python"
    print(
        "Les chaînes de caractères peuvent être indexées avec [] par exemple word = 'python' donc \n word[0]=='p'\n word[5]=='n' \n word[-1]= 'n' ")
    print("word='python' on peut acceder a une sous chaine avce word[0:2] qui sera egale à 'py'")
    print("word[:2] + word[2:] == word", word[:2] + word[2:] == word)
    print("word[42] renvoie erreur mais word[42:] = '' et word[4:42]='on' ")
    print("les string sont immutable en python")
    print("pour une chaine différente il faut en creer une autre ")
    print("obtenir la longeure d\'une chaîne se fait via la fonction len()", len(word))
    print()


def lists():
    squares = [1, 4, 9, 16, 25]
    print(squares)
    print("squares[0] = ", squares[0])
    print("squares[-1] = ", squares[-1])
    print("squares[:2] = ", squares[:2])
    print("squares[:] = ", squares[:])
    print("squares + [36, 49, 64, 81, 100] = ", squares + [36, 49])
    squares[0] = 0
    print("avec squares[0]=0 on a squares égale = ", squares)
    squares.append(1)
    print("en faisant squares.append(1) on obtient", squares)
    squares[2:4] = [34, 45]
    print("en faisant squares[2:4] = [34,45] on obtient ", squares)
    squares[2:4] = [30, 40, 50]
    print("en faisant squares[2:4] = [3,4,5] on obtient ", squares)
    squares[2:4] = []
    print("en faisant squares[2:4] = [] on obtient ", squares)
    print("len pour avoir la longeur d\'une liste ", len(squares))
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print("créer des listes contenant d’autres listes comme ", x)
    print("pour acceder à la premiere liste on fait x[0]", x[0])
    print("pour acceder au premier element de la premiere liste on fait x[0][0]", x[0][0])


def fibonacci():
    print("display the n first elements of fibonacci series")
    n = 0
    a = 0
    b = 1
    while n < 10:
        print(b)
        c = a
        a = b
        b = c + b
        n += 1


def fibonacciV2():
    print("display the n first elements of fibonacci series V2")
    n = 0
    a, b = 0, 1
    while n < 10:
        print(b)
        a, b = b, a + b
        n += 1


def siAndInput():
    x = int(input("Please enter an integer: "))
    if x % 2 == 0 and x >= 0:
        print("positif and pair")
    elif x % 2 == 0 and x < 0:
        print("negatif and pair")
    elif x % 2 != 0 and x < 0:
        print("negatif and impair")
    else:
        print("positif and impair")


def pour():
    words = ['married', 'widow', 'divorced']
    for word in words:
        print(word, len(word))


def pour_range():
    for i in range(5):  # for i in range(0,5)
        print(i)
    for i in range(0, 10, 3):  # with step=3
        print(i)


def arret_continue_with_prime_numbers():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:  # else with for is like try
            print(n, 'is a prime number')
    for num in range(2, 10):
        if num % 2 == 0:
            print("pair number", num)
            continue
        print("impair number", num)


def func_fib_with_prams(n):  # func_fib until n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


def func_fib_with_prams_with_return(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


def ask_ok(prompt, retries=4, reminder='Please try again!'):  # func with defaults valus
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def anonymous_function_with_lambda(n):
    return lambda x: x * n


def sdd():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.extend(["pineapple", "pompous"])
    print(fruits)
    fruits.append(["pineapple", "pompous"])
    print(fruits)
    fruits.insert(2, "strawberry")
    print(fruits)
    fruits.remove("banana")
    print(fruits)  # one occurrence of the element
    fruits.pop(2)  # will delete strawberry
    print(fruits)
    # fruits.clear()
    print(fruits.index("banana"))
    print(fruits.count("apple"))  # nb of occurrences
    fruits.pop()  # remove the last element
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)
    # use lists as stacks
    stack = [1, 2, 3]
    print(stack)
    stack.append(4)
    print(stack)
    stack.pop()
    print("LIFO with pop()->", stack)
    # use lists as queues
    queue = deque([1, 2, 3])
    print(queue)
    queue.append(4)
    queue.append(5)
    print(queue)
    queue.popleft()  # FIFO
    print("FIFO -> ", queue)
    # list of squares
    squares = list(map(lambda x: x ** 2, range(10)))
    print(squares)
    print("une autre maniere de parcourir les lists", [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
    # map equivalent in pyhton
    vec = [-4, -2, 0, 2, 4]
    print(vec)
    vec_map = [x ** 2 for x in vec]
    print(vec_map)
    vec_filter = [x for x in vec if x >= 0]
    print(vec_filter)
    vec_map2 = [abs(x) for x in vec]
    print(vec_map2)
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    foreach = [item.strip() for item in freshfruit]
    print(freshfruit)
    print(foreach)
    # tuples
    tuples = [(item.strip(), len(item.strip())) for item in freshfruit]
    print(tuples)
    # flat a list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_flatten = [number for element in matrix for number in element]
    print(matrix)
    print(matrix_flatten)
    # listes imbriquées
    matrix_inv = [[row[i] for row in matrix] for i in range(3)]
    print(matrix_inv)
    matrix_inv2 = list(zip(*matrix))
    print(matrix_inv2)
    # set
    fruitss = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(fruitss)
    a = set('abracadabra')
    b = set('shazam')
    print("a= ", a)
    print("b=", b)
    print("a - b   ", a - b)  # letters in a but not in b
    print("a | b ", a | b)  # a union b
    print("a & b", a & b)  # a inter b
    print("a ^ b", a ^ b)  # a oux b
    # dictionnaires { key:value}
    tel = {'jack': 4098, 'sape': 4139}
    print(tel)
    # ajouter un element
    tel['guido'] = 4127
    print(tel)
    # supprimer un element
    del tel['sape']
    print(tel)
    # update element
    tel['jack'] = 9099
    print(tel)
    listofkeys = list(tel.keys())
    print(listofkeys)
    listofvalus = list(tel.values())
    print(listofvalus)
    # build dict 1
    dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dict1)
    # build dict 2
    dict2 = {x: x ** 2 for x in range(6)}
    print(dict2)
    # build dict 3
    dict3 = dict(sap=4139, guid=4127, jackk=4098)
    print(dict3)
    # boucles techniques
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():  # iterer sur un dictionnaire
        print(k, v)
    for i in reversed(range(1, 10, 2)):  # iteration inversé
        print(i)


def modules():
    print(fibo.fib2(100))
    print(fibo.__name__)
    varfib = fibo.fib2
    print(varfib(100))
    print(dir())
    # paquets


def inOut():
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    print('The value of PI is approximately %5.3f.' % math.pi)
    print(json.dumps([1, 'simple', 'list']))


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers()
    str()
    lists()
    fibonacci()
    fibonacciV2()
    # siAndInput()
    pour()
    pour_range()
    arret_continue_with_prime_numbers()
    func_fib_with_prams(10)
    print()
    print(func_fib_with_prams_with_return(10))

    anonymous = anonymous_function_with_lambda(3)
    print(anonymous(2))
    print(anonymous(5))
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])  # sort with the first char of each string with anonymous func
    print(pairs)
    sdd()
    modules()
