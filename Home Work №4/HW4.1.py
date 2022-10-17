a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

disc = b ** 2 - 4 * a * c
print(disc)
if disc == 0:
    print(f"x = {-b / 2 * a}")
elif disc < 0:
    print("Нет корней")
else:
    x1 = (-b + disc ** 0.5) / (2 * a)
    x2 = (-b - disc ** 0.5) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")