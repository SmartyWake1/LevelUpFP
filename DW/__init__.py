import requests

page = 1
while True:
    resp = requests.get(f'https://www.wildberries.ru/catalog/sport/elektrotransport-i-aksessuary?sort=popular&page=2').json()
    page += 1
    prod = resp['data']['products']
    if not prod:
        break
    for model in prod:
        print('Бренд:', model['brand'])
        print('Цена:', model['salePriceU'] / 100, "руб.")

    index = model['id']
    id_c = str(index)[:-4]
    for num in range(1, model['pics'] + 1):
        img = f"https://images.wbstatic.net/c516x688/new/{id_c}0000/{index}-{num}.jpg"
        print(img)
        # img = f"https://images.wbstatic.net/big/new/{id_c}0000/{index}-{num}.jpg"
        # print(img)
        # img = f"https://images.wbstatic.net/c246x328/new/{id_c}0000/{index}-{num}.jpg"
        # print(img)