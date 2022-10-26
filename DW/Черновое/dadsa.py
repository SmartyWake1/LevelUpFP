import requests

url = 'https://search.wb.ru/exactmatch/ru/common/v4/search?' \
      '&curr=rub' \
      '&lang=ru' \
      '&locale=ru' \
      '&query=водолазки' \
      '&resultset=catalog' \
      '&sort=popular' \
      '&page=1'
resp = requests.get(url)
prod = resp.json()['data']['products']
dd = []
for model in prod:
    print('Бренд:', model['brand'])
    print('Цена:', model['salePriceU'] / 100, "руб.")

    https://search.wb.ru/exactmatch/ru/common/v4/search?&urr=rub&lang=ru&locale=ru&query=водолазки&resultset=catalog&sort=popular&page=1