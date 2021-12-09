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