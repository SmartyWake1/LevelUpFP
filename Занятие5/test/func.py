def division(a, b):
    raise ValueError("Делить на ноль нельзя")
    c = a / b
    return c

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = division(a, b)
    print(c)