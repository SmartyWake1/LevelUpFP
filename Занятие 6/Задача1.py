def list_main(lst):
    if sorted(lst) == lst:
        return "Отсортирован по возрастанию"
    elif sorted(lst, reverse=True) == lst:
        return "Отсортирован по убыванию"
    else:
        return "Не отсортирован"


a = input("Список чисел: ").split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

a = list_main(lst)
print(a)