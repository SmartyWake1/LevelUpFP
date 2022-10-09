"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
def change(lst):
    b = len(lst) - 2
    c = 0
    for i in range(0, b):
        if lst[1 + i] > lst[0 + i] and lst[1 + i] > lst[2 + i]:
            lst_proofed.append(int(1))
            c += 1
    return c

lst_proofed = []
a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

change(lst)
bc = c
print("Количество элементов списка: ", len(lst))
print("Количество циклов проверки: ", len(lst) - 2)
print("Введеный список: ", lst)
print("Результат проверки: ", lst_proofed)
print("Ответ: ", sum(lst_proofed))
print("Ответ: ", c)