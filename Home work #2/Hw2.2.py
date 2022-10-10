"""Написать программу, считывающую список чисел и выводящую:

!Дополнительно: Реализовать функцию для поиска среднего арифметического, принимающую на вход список и возвращающую число:
a. минимальное число (подсказка)

б. максимальное число (подсказка)

в. среднее арифметическое чисел из списка (подсказка)

г. отсортированный список (подсказка)
список 2 49 3 12 4 56 32 2 49 0 2 1

"""
def minlist(list):
    print("Минимальное число списка: ", min(list))
def maxlist(list):
    print("Максимальное значение списка: ", max(list))
def meanlist(list):
    c = sum(list) / len(list)
    return c
def sortlist(list):
    print("Отсортированный список: ", sorted(list))

a = input("Ввести список чисел: ").split()
list = []
for i in range(len(a)):
    list.append(int(a[i]))
print("Введеный список: ", list)

b = input(str("введите необходимое действие (min,max,mean,sort): "))
b = b.lower()
if b == "min":
   minlist(list)
elif b == "max":
    maxlist(list)
elif b == "mean":
    c = meanlist(list)
    print("Среднее арифметическое: ", c)
elif b == "sort":
    sortlist(list)
else:
    print("Некорректный ввод", b)