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