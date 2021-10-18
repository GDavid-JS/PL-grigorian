# Вариант 4
# Пункт 1
N = int(input("___________\nВведите длину массива: "))
array = []

for i in range(0, N):
    element = int(input("Значение массива: "))
    array.append(element)

max = array[0]
for i in range(0, N):
    if max < array[i]:
        max = array[i]
print("Индекс: " + str(array.index(max)),"\nМаксимальное число: " + str(max))
# Пункт 2
N = int(input("___________\nВведите длину массива: "))
array = []
arrayOdd = []

for i in range(0, N):
    element = int(input("Значение массива: "))
    array.append(element)
    if element % 2:
        arrayOdd.append(element)
if len(arrayOdd) == 0:
    print("Нечетных чисел нет")
print(arrayOdd)

arrayOdd.sort()
arrayOdd.reverse()
print(arrayOdd)


# Вариант 1
# Пункт 1
N = int(input("Введите длину массива: "))
array = []

for i in range(0, N):
    array.append(int(input("Значение массива: ")))

max = array[0]
for i in array:
    if max < i:
        max = i


array.reverse()
print(array, max)



# Пункт 2
N = int(input("________________\nВведите длину массива: "))
array = []

sum = 0
for i in range(0, N):
    element = int(input("Значение массива: "))
    array.append(element)
    sum += element
average = sum/N

for i in range(0, N):
    if array[i] == 0:
        array[i] = average
print(array)

N = int(input("Введите длину массива: "))
array = []

# Вариант 2
# Пункт 1
N = int(input("___________\nВведите длину массива: "))
array = []

for i in range(0, N):
    array.append(int(input("Значение массива: ")))

min = array[0]
for i in array:
    if min > i:
        min = i
print("Минимальное число: " + str(min))

for i in range(0, N):
    if min == array[i]:
        print("Индекс минимального числа: " + str(i))
# Пункт 2
N = int(input("___________\nВведите длину массива: "))
array = []
arrayPositive = []
arrayNegative = []

for i in range(0, N):
    array.append(int(input("Значение массива: ")))

for i in array:
    if i > 0:
        arrayPositive.append(i)
    elif i < 0:
        arrayNegative.append(i)
print(arrayPositive, arrayNegative)
# Вариант 3
# Пункт 1
N = int(input("___________\nВведите длину массива: "))
D = []
sum = 0

for i in range(0, N):
    D.append(int(input("Значение массива: ")))
    if i % 2:
        sum += D[i]
print(D, sum)

# Пункт 2
N = int(input("___________\nВведите длину массива: "))
array = []

for i in range(0, 8):
    element = int(input("Значение массива: "))
    if element < 15:
        element *= 2
    array.append(element)
print(array)
# Вариант 5
# Пункт 1
print("___________")
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)


for i in range(0, 10):
    if i < 10:
        if array[i] < 0 and array[i+1] < 0:
            print(array[i], array[i+1])