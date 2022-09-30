a = 100
i = 10
while i > 0:
    print(a / i)
    i -= 1

a = 100
i = 10
while True > 0:
    print(a / i)
    i -= 1


a = 100
i = 10
while True:
    i -= 1
    if i == 0:
        continue

    if i < -10:
        break
    print(a / i)



for i in range(30):
    print(i)
    if i == 6:
        break