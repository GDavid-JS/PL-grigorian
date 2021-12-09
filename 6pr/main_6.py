# Вариант 6
# Пункт 1
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

max = array[0]
for i in range(0, 10):
    if max < array[i]:
        max = array[i]

firstCounter = 0
secondCounter = 0
for i in array:
    if max > i:
        firstCounter+=1
    elif max < i:
        secondCounter+=1

print(max, firstCounter, secondCounter)

# Пункт 2
array = []

for i in range(0, 10):
    element = int(input("Значение массива: "))
    array.append(element)

sum = 0
for i in array:
    if i > 5:
        sum += i
print(sum)
