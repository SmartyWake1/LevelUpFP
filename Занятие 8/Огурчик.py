                                                  #Mr_pickle
import pickle
a = input("Питон - змея? ")
b = input("Зачем нужен джесок? ")
c = input("А огуречки солёные? ")

My_dict = {1: a, 2: b, 3: c}
with open('OgyrezFile.pickle', "bw") as Ogyrez_file:
    pickle.dump(My_dict, Ogyrez_file)

with open('OgyrezFile.pickle', "br") as Ogyrez_file:
    My = pickle.load(Ogyrez_file)
    print(My)
score = 0
if My[1] in "1":
    score += 1
if My[2] in "2":
    score += 1
if My[3] in "3":
    score += 1
print(score)

                                                    #json
import json
My_dict = {1: a, 2: b, 3: c}
with open('NosokFile.json', "w") as f:
    json.dump(My_dict, f)

with open('NosokFile.json') as f:
    My1 = json.load(f)
    print(My1)

score1 = 0
if My1["1"] in "1":
    score1 += 1
if My1["2"] in "2":
    score1 += 1
if My1["3"] in "3":
    score1 += 1
print(score1)