# Вариант 5
# Пункт 1
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)


for i in range(0, 10):
    if i < 10:
        if array[i] < 0 and array[i+1] < 0:
            print(array[i], array[i+1])

# Пункт 2
array = []
indices = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

for i in range(len(array)):
    for k in range(i+1, len(array)):
        if array[i] == array[k]:
            indices.append(k)
            break
print(array)
for i in range(len(indices)):
    array.pop(indices[i])
    for i in range(len(indices)):
        indices[i] = indices[i]-1
print(array)