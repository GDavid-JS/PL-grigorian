from math import fabs
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
N = int(input("Введите длину массива: "))
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
N = int(input("Введите длину массива: "))
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
N = int(input("Введите длину массива: "))
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
N = int(input("Введите длину массива: "))
D = []
sum = 0

for i in range(0, N):
    D.append(int(input("Значение массива: ")))
    if i % 2:
        sum += D[i]
print(D, sum)

# Пункт 2
N = int(input("Введите длину массива: "))
array = []

for i in range(0, 8):
    element = int(input("Значение массива: "))
    if element < 15:
        element *= 2
    array.append(element)
print(array)

# Вариант 4
# Пункт 1
N = int(input("Введите длину массива: "))
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
N = int(input("Введите длину массива: "))
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

# Вариант 5
# Пункт 1
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)


for i in range(0, 10):
    if i < 10:
        if array[i] < 0 and array[i+1] < 0:
            print(array[i], array[i+1])

# Пункт 2
array = []
indices = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

for i in range(len(array)):
    for k in range(i+1, len(array)):
        if array[i] == array[k]:
            indices.append(k)
            break
print(array)
for i in range(len(indices)):
    array.pop(indices[i])
    for i in range(len(indices)):
        indices[i] = indices[i]-1
print(array)

# Вариант 6
# Пункт 1
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

max = array[0]
for i in range(0, 10):
    if max < array[i]:
        max = array[i]

firstCounter = 0
secondCounter = 0
for i in array:
    if max > i:
        firstCounter+=1
    elif max < i:
        secondCounter+=1

print(max, firstCounter, secondCounter)

# Пункт 2
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

sum = 0
for i in array:
    if i > 5:
        sum += i
print(sum)

# Вариант 7
# Пункт 1
array = []

sum = 0
mulitiplication = 1
for i in range(0, 5):
    element = int(input("Значение массива: "))
    array.append(element)

for i in range(0, 5):
    if i%2:
        mulitiplication*= array[i]
    else:
        sum += array[i]
print(mulitiplication, sum)
# Пункт 2
array = []

for i in range(0, 5):
    element = int(input("Значение массива: "))
    array.append(element)

min = max = array[0]
for i in array:
    if max < i:
        max = i
    if min > i:
        min = i

maxIndex = array.index(max)
minIndex = array.index(min)

array[maxIndex] = min
array[minIndex] = max
print(array)

# Вариант 8
# Пункт 1
array = []

for i in range(0, 5):
    element = int(input("Значение массива: "))
    array.append(element)

sum = 0
mulptiplication = 1
for i in array:
    sum+=i
    mulptiplication*=i
print(sum, mulptiplication)

# Пункт2
array = []
N = 5

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

# Вариант 9
# Пункт 1
N = int(input("Введите длину массива: "))
array = []

for i in range(0, N):
    array.append(float(input("Значение массива: ")))

min = fabs(array[0])
for i in array:
    if min > fabs(i):
        min = fabs(i)
print(min)
array.reverse()
print(array)
# Пункт 2
A = [1, 2, 657, 45, 9, -1, 43, 14, 642, 1345]
B = [24, 6735, 13, 6, 999,666,443,5,1115,86]
print("А: ", A, "B: ", B)
C = []
C = A
A = B
B = C
print("А: ", A, "B: ", B)
# Вариант 10
# Пункт 1
array = [1, 43, 3453]
mean = None
for i in range(len(array)):
    for k in range(i+1, len(array)):
        if array[i] == array[k]:
            mean = array[k]
            break
if not mean:
    print("Повторяющиеся элементы отсутсвуют!")
else:
    print(mean)
# Пункт 2
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 123, 32, 10, 15, 24, 54]
arrayCopy = array.copy()
for i in range(len(array)):
    if array[i] < 10:
        array[i] = 0
    elif array[i] > 20:
        array[i] = 1
print(arrayCopy,array)
# Вариант 11
# Пункт 1
arr = [1, 532, 34, 645, 647]

max = arr[0]
for i in arr:
    if not i%2 and max < i:
        max = i
        
print(max)
# Пункт 2
arr = [64, 6, 10, 4, 5, 1, 7]
newArr = []

for i in arr:
    if i < 10 and not i%2:
        newArr.append(i)
if len(newArr):
    newArr.sort()
    print(newArr)
else:
    print("Четных чисел меньше десяти нет!")
# Вариант 12
# Пункт 1
arr = [1, -1, 5, 6, 8]
min = arr[0]
for i in arr:
    if i%2 and min > i:
        min = i
print(min)
# Пункт 2
A = [1, 2, 657, 45, 9, -1, 43, 14, 642, 1345]
B = [24, 6735, 13, 6, 999,666,443,5,1115,86]
C = []
C = A
A = B
B = C
print("А: ", A)
print("B: ", B)
# Вариант 14
# пунтк 1
array = [1, 3, 65, 2]
min = max = array[0]
for i in array:
    if max < i:
        max = i
    if min > i:
        min = i

maxIndex = array.index(max)
minIndex = array.index(min)

array[maxIndex] = min
array[minIndex] = max
print(array)
# пункт 2
array = []
N = 5

for i in range(0, N):
    array.append(int(input("Значение массива: ")))

sum = 0
for i in range(0, N):
    sum += array[i]
average = sum/N

for i in range(0, N):
    if array[i] > average:
        array[i] = 1
print(array)
# Вариант 15
# Пункт 1
array = [1, 1, 1, 4, 6]
for i in range(len(array)):
    for k in range(i+1, len(array)):
        if array[i] == array[k]:
            print(array[k])
            break
# Пункт 2
array = [1, 2, 3, 4, 5, 6, 7, 8, 8]
arrayOdd = []

for i in range(len(array)):
    if array[i] % 2:
        arrayOdd.append( array[i])
if not len(arrayOdd):
    print("Нечетных чисел нет")
# print(arrayOdd)

arrayOdd.sort()
arrayOdd.reverse()
print(arrayOdd)