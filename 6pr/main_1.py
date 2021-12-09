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