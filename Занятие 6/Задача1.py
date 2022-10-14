
def list_main(lst):
    if sorted(lst) == lst:
        return True
    elif sorted(lst, reverse=True) == lst:
        return True
    else:
        return False

if __name__ == "__main__":
    a = input("Список чисел: ").split()
    lst = []
    for i in range(len(a)):
        lst.append(int(a[i]))

    a = list_main(lst)
    print(a)