import statistics

def read_input():
    n = int(input("введите число"))
    my_list = []
    for i in range(n):
      number = int(input())
      my_list.append(number)
    return my_list

my_list = read_input()
mean_number = statistics.mean(my_list)
print("Среднее значение", mean_number)

larger = []
smaller = []
for i in my_list:
    if i >= mean_number:
        larger.append(i)
        print(f"Выше среднего {larger}'")
    elif i < mean_number:
        smaller.append(i)
        print(f"Ниже среднего {smaller}")