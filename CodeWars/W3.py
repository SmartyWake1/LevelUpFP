"""
Банкоматы позволяют использовать 4- или 6-значные PIN-коды, а PIN-коды не могут содержать ничего, кроме ровно 4 или ровно 6 цифр.

Если функции передана допустимая строка PIN-кода, верните true, иначе верните false.

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


"""
pin = input()
a = str(pin)
b = a.isdigit()
if b == True:
    if len(a) == 4:
        print(True)
    elif len(a) == 6:
        print(True)
    else:
        print(False)
else:
    print(False)