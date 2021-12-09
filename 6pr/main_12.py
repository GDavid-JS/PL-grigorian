# Вариант 12
# Пункт 1
arr = [1, -1, 5, 6, 8]
min = arr[0]
for i in arr:
    if i%2 and min > i:
        min = i
print(min)
# Пункт 2
A = [1, 2, 657, 45, 9, -1, 43, 14, 642, 1345]
B = [24, 6735, 13, 6, 999,666,443,5,1115,86]
C = []
C = A
A = B
B = C
print("А: ", A)
print("B: ", B)