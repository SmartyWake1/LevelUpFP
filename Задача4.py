n = int(input())
b = 2
for a in range(0, n+b):
    if a % b ==0 and not a == 0:
        print(a)