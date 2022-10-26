import json

def analysis():
    with open("ParserRusultURL.json", "r", encoding="utf8") as File_analysis:
        a = json.load(File_analysis)
        print(a)
        for key in a:
            print(a[key])
            for Price in a[key]:
                print(a[key][Price])

if __name__ == "__main__":
    analysis()