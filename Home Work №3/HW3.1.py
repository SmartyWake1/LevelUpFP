def enter_input():
    My_input = input("Введите числа через пробел: ")
    f = My_input.replace("-", "")
    c = f.replace(" ", "")
    if c.isdigit() == False:
        return False
    else:
        My_input = My_input.split()
        list = []
        for i in range(0, len(My_input)):
            a = My_input[0 + i]
            list.append(int(a))
        return list

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



choice_input = int(input("Метод через пробел/Метод через кол-во(1/2): "))
if choice_input == 1:
    result = enter_input()
elif choice_input == 2:
    result = enter_input2()
print(result)