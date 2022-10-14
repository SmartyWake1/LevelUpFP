My_dict1 = [1, 2, 3, 4]
My_dict2 = [1, 4, 9, 16]
print(dict(zip(My_dict1, My_dict2)))

My_dict3 = {}
for i in range(0, len(My_dict1)):
    My_dict3[My_dict1[i]] = My_dict2[i]
print(My_dict3)