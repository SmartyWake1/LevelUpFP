import json

def analysis():
    with open("ParserRusult.json", "r", encoding="utf8") as File_analysis:
        a = json.load(File_analysis)
        print(a)



analysis()