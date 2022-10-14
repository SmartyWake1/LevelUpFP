"""
Возвращает количество (количество) гласных в заданной строке.

Мы будем рассматривать a, e, i, o, uкак гласные для этой Ката (но не y).

Входная строка будет состоять только из строчных букв и/или пробелов.
def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in inputStr:
        if i in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1
        else:
            pass
    return num_vowels
"""

sentence = "by"
sentence = list(sentence)
print(list(sentence))
print(len(sentence))

a = 0
for i in range(0, len(sentence)):
    if "a" in sentence:
        a += 1
        sentence.remove("a")
    elif "e" in sentence:
        a += 1
        sentence.remove("e")
    elif "i" in sentence:
        a += 1
        sentence.remove("i")
    elif "o" in sentence:
        a += 1
        sentence.remove("o")
    elif "u" in sentence:
        a += 1
        sentence.remove("u")

print(a)