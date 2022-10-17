a = input("3 числа: ").split()

disc = int(a[1]) ** 2 - 4 * int(a[0]) * int(a[2])
print("Диск", disc)

if disc == 0:
    print(f"x = {-int(a[1]) / 2 * int(a[0])}")

elif disc < 0:
    print("Нет корней")

else:
    x1 = (-int(a[1]) + disc ** 0.5) / (2 * int(a[0]))
    x2 = (-int(a[1]) - disc ** 0.5) / (2 * int(a[0]))
    print(f"x1 = {x1} \nx2 = {x2}")
