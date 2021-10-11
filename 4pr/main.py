print("https://github.com/GDavid-JS/PL-grigorian")
a = int(input("Введите число А "))
b = int(input("Введите число Б "))

#Первая задача
for i in range(a, b+1):
   print(i)


#Вторая задача
a = int(input("Введите число А "))
b = int(input("Введите число Б "))
i = a
if a < b:
    while i<=b:
        print(i)
        i+=1
else:
    while i >= b:
        print(i)
        i -= 1

#Третья задача
a = int(input("Введите число А "))
i = a
while i > b:
    i -=1
    if i % 2 == 1:
        print(i)

#Четвертая задача
N = int(input("Введите число N "))
sum = 0
for i in range(0, N):
    sum += int(input("Введите число: "))
print(sum)

#Пятая задача
n = int(input("Введите число n "))
sum = 0
for i in range(1, n + 1):
   sum += i**3
print(sum)

#Шестая задача
n = int(input("Введите число n: "))
mulplication = 1;
for i in range(1, n+1):
    mulplication*=i
print(mulplication)

#седьмая задача
n = int(input("Введите число n: "))
multiplication = 1
sum = 0
for i in range(1, n+1):
    multiplication*= i
    sum += multiplication
print(a)

#восьмая задача
n = int(input("Введите число n: "))
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end = "")
    print("\n")

#девятая задача
n = int(input("Введите число N: "))
f1 = 0
f2 = 1
f3 = 0
i = 0
while i < n-2:
    fSum = f1 + f2
    f1 = f2
    f2 = fSum
    f3 += fSum
    i +=1
print(f3+1)

#десятая задача
N = int(input('Количество чисел из ряда Фибоначи: '))
K = int(input('Порядковый номер в ряду: '))

arr = [0, 0, 0]
sum = 0

for i in range(0, N):
    if i == 1:
        arr[2] = 1
        arr[1] = 1
    if i >= K-1:
        sum += arr[2]
    arr[2] = arr[0] + arr[1]
    arr[0] = arr[1]
    arr[1] = arr[2]
print(sum)