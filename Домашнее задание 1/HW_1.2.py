month_number = int(input("Введите номер месяца: "))
month_list = [3, 5, 7, 8, 10, 12]
if 0 >= month_number or month_number > 12:
    print("Такого номера месяца не существует!")
elif month_number == 2:
    print("Февраль")
elif month_number in month_list:
    print("31 день в месяце")
else:
    print("30 дней в месяце")