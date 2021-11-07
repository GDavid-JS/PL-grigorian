# Вариант 4
# Пункт 1
A = int(input())
B = int(input())
C = int(input())
D = int(input())


def division(a, b):
    return [b, a/b, a%b]

def NOD(a, b):
    result = division(a,b)

    while result[2] != 0:
        result = division(result[0], result[2])
    if result[2] == 0:
        return result[0]
    # elif result[2] == 0:
    #     return

numerator = A * D
denominator = B * C
nod = NOD(numerator, denominator)
print(numerator // nod, '/', denominator // nod)

# Пункт 2
a = int(input("Введите координату центра окружности a: "))
b = int(input("Введите координату центра окружности b: "))
Radius = int(input("Введите радиус: "))

def ex(x, y):
    if pow(x-a, 2)+pow(y-b, 2) <= Radius**2:
        return True
    else:
        return False

coordinates = [["р1", "р2"], ["f1", "f1"], ["l1", "l2"]]
counter = 0
for i in coordinates:
    x = int(input(f'Введите координату {i[0]}: '))
    y = int(input(f'Введите координату {i[1]}: '))
    if ex(x, y):
        counter += 1
print(counter)
