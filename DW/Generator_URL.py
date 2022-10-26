import json

def Generator_URL():
    with open("ParserRusult.json", "r", encoding="utf8") as File_analysis_in:
        with open("ParserRusultURL.json", "w", encoding="utf8") as File_analysis_from:
            a = json.load(File_analysis_in)
            print(len(a))
            print(a)
            for key in a:
                print(a[key])
                for Price in a[key]:
                    print(a[key][Price])
                    id = a[key][Price]
                    GenURL = f"https://www.wildberries.ru/catalog/{id}/detail.aspx?targetUrl=XS"
                    print(GenURL)
                    a[key][Price] = GenURL
            json.dump(a, File_analysis_from)
        print(a)

if __name__ == "__main__":
    Generator_URL()