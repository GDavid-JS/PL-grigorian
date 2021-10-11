print("Первый вариант")
string = input("Введите строку(русский язык): ");
string_arr = string.split(' ')
j = 0
for i in string_arr:
    if i[0] == 'е':
        j+=1
print(j)

print("Второй вариант")
string = input("Введите строку(любой язык): ");
j = 0
for i in range(0, len(string)):
    if string[i] == ':':
        j+=1
string = string.replace(':', '%')
print(string, "\nКол-во замен: " + str(j))

print("Третий вариант")
string = input("Введите строку(любой язык): ");
j = 0
for i in range(0, len(string)):
    if string[i] == '.':
        j+=1
string = string.replace(".", "")
print(string, "\nКол-во удаленных символов: " + str(j))

print("Четвертый вариант")
string = input("Введите строку(русский язык): ");
j = 0

for i in range(0, len(string)):
    if string[i] == 'а':
        j+=1

string = string.replace('а', 'о')
print(string,"\n" + str(len(string)), "\nКол-во замен = " + str(j))

print("Пятый вариант")
print(input("Введите строку(любой язык): ").lower())

print("Шестой вариант")
string = input("Введите строку(русский язык): ");
j = 0
for i in range(0, len(string)):
    if string[i] == 'а':
        j+=1
string = string.replace("а", "")
print(string, "\nКол-во удаленных символов: " + str(j))

####
print("Седьмой вариант")
print("Может работать только с четным количеством символов по объективным причинам")
string = input("Введите строку(русский язык): ");
newstring = ""
j = int(len(string)/2)
for i in range(0, j): newstring += string[i]
print(string.replace(string[:j], newstring.replace('п', '*')))

print("Восьмой ваниант")
print(len(input("Введите строку(любой язык): ").split()))

print("Девятый ваниант")
string1 = input("Введите строку: ");
string2 = input("Введите слово: ");
j = 0
for i in string1.split():
    if i == string2:
        j += 1
print(j)

print("Десятый ваниант")
array = input("Введите строку(английский язык): ").split()
for i in range(0, len(array)): array[i] = array[i].replace(array[i][0], array[i][0].upper(), 1)
print(" ".join(array))

print("Одинаддцатый ваниант")
string = input("Введите строку(русский язык): ")

iterator = 1
max = 0
for i in range(1, len(string)):
    if string[i] == string[i-1] == 'н':
        iterator += 1
        if iterator > max:
            max = iterator
    else:
        iterator = 1
print(max)
print(string.replace(".", "!"))

print("Двенадцатый ваниант")

for i in input("Введите строку(русский язык): ").split(" "):
    if i[len(i)-1] == 'я':
        print(i)

print("Тринадацатый ваниант")
string = input("Введите строку(любой язык): ")
print(string[string.find('(') + 1:string.find(')')])

print("Четырнадцатый ваниант")
for i in input("Введите строку(русский язык): ").split(" "):
    if i[len(i)-1] == 'я' or i[0] == 'а' :
        print(i)

print("Пятнадцатый ваниант")
iterator = 0
for i in input("Введите строку(русский язык): "):
    if i == 'т':
        iterator += 1
print(iterator)