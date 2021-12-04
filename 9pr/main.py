#Пунктт 1
file = open("D:\\python\\9pr\\grigoryan_david_zhirayrovich_уб-12_vvod.txt")
array = []

for line in file:
    arr = []
    string = line.strip().split(" ")
    for i in string:
        arr.append(int(i))
    array.append(arr)
print(array)
file.close()

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

file = open("D:\\python\\9pr\\grigoryan_david_zhirayrovich_уб-12_vivod.txt", "w", encoding="utf-8")
file.write(f"{array}\n")
file.write(f"Строка с наибольшей суммой элементов: {array[maxIndex]} сумма элементов: {max}\n")
file.write(f"Стркоа с наименьшей суммой элеметнов: {array[minIndex]} сумма элементов: {min}\n")

# Пункт 2
N = int(input("Введите N: "))
array = []

def printArr(arr):
    string = ""
    for i in arr:
        string += "["
        for k in i:
            string += f"{k} "
        string += "]\n"
    return string

for i in range(N):
    array.append([])
    for k in range(N):
        mean = int(input("Введите значение массива: "))
        a = 0 if mean < 0 else 1
        array[i].append(a)
file.write(f"{printArr(array)}\n")
for i in range(N):
    for k in range(N):
        if i < k:
            file.write(f"{array[i][k]}\n")
file.close()