def countRange(lst, lst_min, lst_max):
    list = []
    for i in range(0, len(lst)):
        if lst_max < lst[0 + i] < lst_min:
            continue
        elif lst_max > lst[0 + i] > lst_min:
            list.append(float(lst[0 + i]))
    return list

if __name__ == "__main__":
    a = input("Список чисел: ").split()
    lst = []
    for i in range(len(a)):
        lst.append((float(a[i])))
    lst_max = int(input("Максимальное значение: "))
    lst_min = int(input("Минимальное значение: "))

    c = countRange(lst, lst_min, lst_max)
    print(c)