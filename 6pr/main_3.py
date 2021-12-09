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