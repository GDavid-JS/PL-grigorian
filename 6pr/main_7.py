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