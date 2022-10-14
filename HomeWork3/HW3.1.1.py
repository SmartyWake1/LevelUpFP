def enter_input2():
    a = input("Сколько чисел будет введено: ")
    if a.isdigit() == False:
        print(f"Такой нумерации не может быть ({a})")
        return False
    else:
        lst = []
        i = 1
        for i in range(i, int(a)+1):
            c = input(f"Введите число {i}: ")
            c_check = c.replace("-", "")
            if c_check.isdigit() == False:
                print(f"Некорректный ввод '{c_check}'")
                return False
                break
            else:
                lst.append(int(c))
                if i < int(a):
                    print(f"Вы уже ввели {i} чисел: {lst}")
                else:
                    print("Введеный список чисел - ", lst)
    return(lst)


fd = enter_input2()
print(fd)
