import requests

def parse():
    response = requests.get("https://www.wildberries.ru/catalog/sport/elektrotransport-i-aksessuary?sort=popular&page=2")

    print(response.status_code)
    print(response.text)

    jesik = response.json()
    print(jesik)

    prod = jesik['data']['products']
    for model in prod:
        print('Бренд:', model['brand'])
        print('Цена:', model['salePriceU'] / 100, "руб.")

    index = model['id']
    id_c = str(index)[:-4]
    for num in range(1, model['pics'] + 1):
        img = f"https://images.wbstatic.net/c516x688/new/{id_c}0000/{index}-{num}.jpg"
        print(img)
parse()