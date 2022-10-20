My_dict = {"Конь Бо-Джек": 4, "Машка": 5}
while True:
    UserAction = str(input("Введите команду(add, all, mark, edit, delete, average, exit): ")).lower()
    print(f"Ваша команда__'{UserAction}'")
    if UserAction == "add":                                                     # Функция добавления учеников(работает)
        ActionAdd = input("Введите имя ученика: ").capitalize()
        My_dict[ActionAdd] = None
        print(My_dict)

    elif UserAction == "all":                                                   # Показать список учеников(Работает)
        for key in My_dict:
            print(key)

    elif UserAction == "mark":                                                  # Добавление оценки(Работает)
        ActionAdd = input("Имя ученика: ").capitalize()
        ActionMark = int(input("Оценка: "))
        My_dict.update({ActionAdd: ActionMark})
        print(My_dict)

    elif UserAction == "edit":
        print("Поменять тебя?")
    elif UserAction == "delete":
        print("Лучше удали")
    elif UserAction == "average":
        print("Хахахах")
    elif UserAction == "exit":
        print("До свидания!")
        exit()