"""
Написать программу, считывающую список чисел и выводящую список в обратном порядке.
4 5 6 2 1 6 8 34 2 1
for i in range():
    lst[0 + i]
    c.append()

"""

a = input("Список чисел: ").split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))
print("Введеный список: ", lst)

c = []
i = 0
for i in range(-1, -(len(lst) + 1), -1):
    c.append(int(lst[i]))

print("Зеркальный список: ", c)