def input1():
    a = int(input())
    b = int(input())
    return a, b


def calc(a, b):
    d = a
    for i in range(b):
        d = d + d * 0.1
    print(d)

a, b = input1()
calc(a, b)