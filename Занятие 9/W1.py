lst = []

with open("textline.txt", encoding="utf8") as f:
    b = [line for line in f]
    for i in b:
        if "#" in i:
            k = i.index("#")
            print(k)
            first_five_chars = i[:k] + "\n"
            lst.append(first_five_chars)

        else:
            lst.append(i)

with open("textlinenew.txt", mode="w", encoding="utf8") as p:
    for text in lst:
        p.write(text)

print(lst)