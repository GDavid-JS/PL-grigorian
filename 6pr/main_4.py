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
