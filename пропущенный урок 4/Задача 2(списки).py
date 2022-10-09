"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
# 10 3 1 3 40 10 2 10 9 10 9 10 11 10 (39 минута)
def change(lst):
    b = len(lst) - 2
    for i in range(0, b):
        if lst[1 + i] > lst[0 + i] and lst[1 + i] > lst[2 + i]:
            lst_proofed.append(int(1))

lst_proofed = []
a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

change(lst)
print("Количество элементов списка: ", len(lst))
print("Количество циклов проверки: ", len(lst) - 2)
print("Введеный список: ", lst)
print("Результат проверки: ", lst_proofed)
print("Ответ: ", sum(lst_proofed))

