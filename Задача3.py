a = int(input("Число 1:"))
b = int(input("Число 2:"))
c = int(input("Число 3:"))

if a == b == c:
    print("Одинаковые числа")
if a > b and a > c:
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
if b > a and b > c:
    if a > c:
        print(c, a, b)
    else:
        print(b, a, c)
if c > a and c > b:
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c)