def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

change(lst)
print(lst)