N = int(input('Количество чисел из ряда Фибоначи: '))
K = int(input('Порядковый номер в ряду: '))

arr = [0, 0, 0]
sum = 0

for i in range(0, N):
    # print(i)
    if i == 1:
        arr[2] = 1
        arr[1] = 1
    if i >= K-1:
        sum += arr[2]
    arr[2] = arr[0] + arr[1]
    arr[0] = arr[1]
    arr[1] = arr[2]
print(sum)