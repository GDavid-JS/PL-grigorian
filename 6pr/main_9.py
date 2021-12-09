# Вариант 9
# Пункт 1
from math import fabs

N = int(input("Введите длину массива: "))
array = []

for i in range(0, N):
    array.append(float(input("Значение массива: ")))

min = fabs(array[0])
for i in array:
    if min > fabs(i):
        min = fabs(i)
print(min)
array.reverse()
print(array)
# Пункт 2
A = [1, 2, 657, 45, 9, -1, 43, 14, 642, 1345]
B = [24, 6735, 13, 6, 999,666,443,5,1115,86]
print("А: ", A, "B: ", B)
C = []
C = A
A = B
B = C
print("А: ", A, "B: ", B)