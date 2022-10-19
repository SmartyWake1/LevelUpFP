import matplotlib.pyplot as plt

a = input("3 числа: ").split()

disc = float(a[1]) ** 2 - 4 * float(a[0]) * float(a[2])
print("Диск", disc)

if disc == 0:
    x1 = -float(a[1]) / 2 * float(a[0])
    x2 = -float(a[1]) / 2 * float(a[0])
    print(f"x = {-float(a[1]) / 2 * float(a[0])}")

elif disc < 0:
    print("Нет корней")

else:
    x1 = (-float(a[1]) + disc ** 0.5) / (2 * float(a[0]))
    x2 = (-float(a[1]) - disc ** 0.5) / (2 * float(a[0]))
    print(f"x1 = {x1} \nx2 = {x2}")

x_coords = []
y_coords = []

# parabola_func = (int(a[0]) * x ** 2) + (int(a[1]) * x) - int(a[2])
for i in range(0, 50):
    x_coords.append(x1 + i - 0.9)
    x_coords.append(x2 - i + 0.9)

x_coords = sorted(x_coords)

for i in range(0, len(x_coords)):
    a_p = float(a[0])
    x1_p = float(x_coords[i])
    x1_p1 = float(x1_p ** 2)
    b_p = float(a[1])
    x2_p = float(x_coords[i])
    c_p = float(a[2])
    y_coords.append((a_p * x1_p1) + (b_p * x2_p) + c_p)

plt.plot(x_coords, y_coords)
plt.show()