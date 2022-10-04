def function1():
    a = int(input())
    b = int(input())
    c = input()
    return a, b, c



def calc(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    elif c == "-":
        print(a - b)

a, b, c = function1()
calc(a, b, c)