"""
обро пожаловать. В этой ката вас просят возвести в квадрат каждую цифру числа и соединить их.

Например, если мы пропустим через функцию 9119, получится 811181, потому что 9 2 равно 81, а 1 2 равно 1.

Примечание . Функция принимает целое число и возвращает целое число.
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

"""


num = 9119
if num < 0:
    num *= -1
num = str(num)
b = list(num)
d = []
for i in range(0, len(b)):
    c = b[0 + i]
    c = int(c) ** 2
    c = str(c)
    d.append(c)

f = ""
for i in range(0, len(b)):
    f += d[0 + i]

print(int(f))