import requests
import time
import random
import json
def Parser():
    Pricelist = {}
    page = 1
    while page <= 1:
        resp = requests.get(f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,7,3,6,5,18,21&curr=rub&dest=-1216601,-337422,-1114902,-1198055&emp=0&lang=ru&locale=ru&page={page}&pricemarginCoeff=1.0&query=чехлы на iphone 11&reg=0&regions=80,68,64,83,4,38,33,70,82,69,86,30,40,48,1,22,66,31&resultset=catalog&sort=popular&spp=0&suppressSpellcheck=false').json()
        print("Страница", page)
        time.sleep(random.randint(0, 3))
        page += 1
        prod = resp['data']['products']
        if prod == "":
            break
        for model in prod:
            print('Name:', model['brand'])
            print('Price:', model['salePriceU'] / 100, "руб.")
            print('ID:', model['id'])
            Pricelist[model['brand']] = {model['salePriceU'] / 100: model['id']}
            print(Pricelist)

    with open("ParserRusult.json", "w", encoding="utf8") as file_json:
        json.dump(Pricelist, file_json)


if __name__ == "__main__":
    Parser()