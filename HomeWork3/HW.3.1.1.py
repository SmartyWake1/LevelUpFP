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



d = enter_input()
print(d)
"""
if My_input.isdigit() == True:
for i in My_input:
print(My_input.isdigit()

c = My_input.replace(" ", "")
"""