"""Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""

a = input("Ввести список: ").split()     #1
lst_input = []                           #1
for i in range(len(a)):                  #1
    lst_input.append(int(a[i]))          #1

lst_sorted = sorted(lst_input)           #2
print("уникальных элементов: ", len(set(lst_sorted)))