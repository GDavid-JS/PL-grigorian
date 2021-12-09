# Вариант 8
# Пункт 1
array = []

for i in range(0, 5):
    element = int(input("Значение массива: "))
    array.append(element)

sum = 0
mulptiplication = 1
for i in array:
    sum+=i
    mulptiplication*=i
print(sum, mulptiplication)

# Пункт2
array = []
N = 5

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
