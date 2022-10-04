
my_list = [1, 2, 3, 4]                # список
my_list.append(111)                   # Добавить число в список
my_list.append(True)
my_list.append("my_string")
my_list.append([5, 4, 7])
print(my_list)
print(my_list[0])
print(my_list[-1])

l = len(my_list)                      # длина списка
print(l)

# списки можно складывать, можно умножать на число
my_list.remove(3)                      # удаление из списка элемента с таким же значением
print(my_list)

my_list.sort()
for i in my_list:
    print(i)