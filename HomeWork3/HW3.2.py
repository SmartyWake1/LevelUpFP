def My_input1():
    My_input = input("О: ").split()
    a = int(My_input[0])
    b = int(My_input[2])
    operation = My_input[1]
    return a, b, operation

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if 0 < b > 0:
            return a / b
        else:
            return "Делить на ноль нельзя"


a, b, operation = My_input1()
result = calculate(a, b, operation)
print(f"{a}{operation}{b} = {result}")