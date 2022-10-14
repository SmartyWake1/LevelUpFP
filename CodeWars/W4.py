n = int(input())
list = []

a = n
pred_element = []
for i in range(n, 0, -1):
    pred_element.append(n-i)
    a -= 1

index_first_element = sum(pred_element) + 1

for i in range(0, n):
    b = 1 + 2 *(index_first_element + i - 1)
    list.append(b)

print(sum(list))




return n ** 3




"""
a = 1
for i in range(0, n):
    a += 2
print(1 + 2 *(16 - 1))


index_element = 13*13

"""




"""
Формула прогресси в принте
поиск индекса элемента в переменной

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3
n ** 

"""