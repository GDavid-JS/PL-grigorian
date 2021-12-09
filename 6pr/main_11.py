# Вариант 11
# Пункт 1
arr = [1, 532, 34, 645, 647]

max = arr[0]
for i in arr:
    if not i%2 and max < i:
        max = i
        
print(max)
# Пункт 2
arr = [64, 6, 10, 4, 5, 1, 7]
newArr = []

for i in arr:
    if i < 10 and not i%2:
        newArr.append(i)
if len(newArr):
    newArr.sort()
    print(newArr)
else:
    print("Четных чисел меньше десяти нет!")