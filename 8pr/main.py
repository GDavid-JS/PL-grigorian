#Пунктт 1
array = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [4, 5, 6, 7]
]

arr = []
for i in range(len(array)):
    sum = 0
    for k in array[i]:
        sum += k
    arr.append([sum, i])

min = max = arr[0][0]
maxIndex = 0
minIndex = 0
for i in arr:
    if i[0] > max:
        max = i[0]
        maxIndex = i[1]
    if i[0] < min:
        min = i[0]
        minIndex = i[1]
print(array, "\n")
print("Строка с наибольшей суммой элементов:", array[maxIndex], "Сумма элементов: ", max)
print("Стркоа с наименьшей суммой элеметнов:", array[minIndex], "Сумма элементов: ", min)

# Пункт 2
N = int(input("Введите N: "))
array = []

def printArr(arr):
    for i in arr:
        print("[ ", end = "")
        for k in i:
            print(k, end = " ")
        print("]")

for i in range(N):
    array.append([])
    for k in range(N):
        mean = int(input("Введите значение массива: "))
        a = 0 if mean < 0 else 1
        array[i].append(a)
printArr(array)
for i in range(N):
    for k in range(N):
        if i < k:
            print(array[i][k])