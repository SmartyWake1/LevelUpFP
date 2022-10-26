import requests
def fetch(url, params):
    headers = params["headers"]
    body = None
    if params["method"] == "GET":
        return requests.get(url, headers=headers)
    if params["method"] == "POST":
        return requests.post(url, headers=headers, data=body)


price = fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358949&to=1666394949", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "ticket": "",
    "token": "",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": None,
  "method": "GET"
})
print(price.json().keys())
openPrice = price.json()["o"]
closePrice = price.json()["c"]
print(f"open prince = {openPrice}, \nclose price = {closePrice}")
print(price.json()["scale"])