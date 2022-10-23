My_dict = {"Конь Бо-Джек": 4, "Машка": 5, "Рандомтип": 2}

while True:
    UserAction = str(input("Введите команду(add, all, mark, edit, delete, average, exit): ")).lower()
    print(f"Ваша команда__'{UserAction}'")
    if UserAction == "add":                                                     # Функция добавления учеников(работает)
        ActionAdd = input("Введите имя ученика: ").capitalize()
        My_dict[ActionAdd] = None
        print(f"Ученик '{ActionAdd}' успешно добавлен!")

    elif UserAction == "all":                                                   # Показать список учеников(Работает)
        for key in My_dict:
            print(f"{key}, {My_dict[key]}")

    elif UserAction == "mark":                                                  # Добавление оценки(Работает)
        ActionAdd = input("Имя ученика: ").capitalize()
        if ActionAdd in My_dict:
            ActionMark = int(input("Оценка: "))
            My_dict.update({ActionAdd: ActionMark})
            print(My_dict)
        else:
            print(f"Такого имени не существует '{ActionAdd}'")

    elif UserAction == "edit":                                                  # Изменение имени(ключа)(Работает)
        ActionEdit = str(input("Введите имя ученика ").capitalize())
        if ActionEdit in My_dict:
            NowName = str(input("Введите новое имя ученика ").capitalize())
            My_dict[NowName] = My_dict[ActionEdit]
            My_dict.pop(ActionEdit)
            print(f"Имя успешно изменено с {ActionEdit} на {NowName}")
        else:
            print(f"Такого имени не существует '{ActionEdit}'")

    elif UserAction == "delete":
        print(My_dict.keys())                                   # Удаление ученика(Работает)
        DeleteName = input("Имя ученика: ").capitalize()
        if DeleteName in My_dict:
            My_dict.pop(DeleteName)
            print(f"Ученик '{DeleteName}' удален")
        else:
            print(f"Такого имени не существует '{DeleteName}'")


    elif UserAction == "average":
        a = 0
        for key in My_dict:
            a += My_dict[key]
        print(f"Средний балл учеников = {a / len(My_dict)}")

    elif UserAction == "exit":                                                 # Выход из программы(Работает)
        print("До свидания!")
        exit()
    else:
        print("Такой команды не существует")