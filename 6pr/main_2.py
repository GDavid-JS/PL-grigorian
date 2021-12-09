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