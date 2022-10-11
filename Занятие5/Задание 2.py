horizontal = 1
for i in range(1, 11):
    vertical = 1
    for i in range(1, 11):
        print(horizontal * vertical, end="\t")
        vertical += 1
    print(" ")
    horizontal += 1
