My_dict = {}
letter = input()

for i in letter:
    if i in My_dict:
        My_dict[i] += 1
    else:
        My_dict[i] = 1
print(My_dict)

for k, v in My_dict.items():
    print(f"{k}: {v}")

