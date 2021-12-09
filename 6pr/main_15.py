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