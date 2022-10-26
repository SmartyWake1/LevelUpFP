import json

def Generator_URL():
    with open("ParserRusult.json", "r", encoding="utf8") as File_analysis:
        a = json.load(File_analysis)
        print(len(a))
        print(a)
        for key in a:
            print(a[key])
            for Price in a[key]:
                print(a[key][Price])
                id = a[key][Price]
                GenURL = f"https://www.wildberries.ru/catalog/{id}/detail.aspx?targetUrl=XS"
                print(GenURL)


if __name__ == "__main__":
    Generator_URL()