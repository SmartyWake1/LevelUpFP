import requests
def fetch(url, params):
    headers = params["headers"]
    body = None
    if params["method"] == "GET":
        return requests.get(url, headers=headers)
    if params["method"] == "POST":
        return requests.post(url, headers=headers, data=body)


fetch("https://bcs-express.ru/kotirovki-i-grafiki/yndx", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/kotirovki-i-grafiki/yndx", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/kotirovki-i-grafiki/yndx", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357734&to=1666393734", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357734&to=1666393734", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Bold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Regular-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Semibold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/styles/quotes-item.min.css?v=xcyY95o8cE7Xb4BnKeFoOghxKzq7BMf8-rWp_7WFpuU", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://polyfill.io/v3/polyfill.min.js?features=es6%2Ces2017%2CIntersectionObserver%2CIntersectionObserverEntry%2Cfetch%2CResizeObserver", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/runtime.min.js?v=i5zg03rnFRrdE0cxTxDtC6w3jyWqGZ50wgkSJpE7_Ys", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/vendor.min.js?v=E7uV_riU80FaUrTLNNgpinagiIRwHr9rL7A3mGk_GmM", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/quotes-item.min.js?v=9IHQ6hrnFLifQZXbRbkQhIWvN_GeI7vaPCCGUJKg6W8", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.googletagmanager.com/gtm.js?id=GTM-M84QXK", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjMwMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBvcGFjaXR5PSIuMiIgZD0iTTAgMzE0LjF2LTE3NEMwIDYyLjc4IDYyLjY4LjEgMTQwIC4xaDIwMHYzMTRIMFoiIGZpbGw9InVybCgjYSkiLz48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSIwIiB5MT0iMjU3LjAwOSIgeDI9IjMwMS43NSIgeTI9IjI1Ny4wMDkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjQTlBM0U5Ii8+PHN0b3Agb2Zmc2V0PSIuOTAxIiBzdG9wLWNvbG9yPSIjQTlBM0U5IiBzdG9wLW9wYWNpdHk9IjAiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google-analytics.com/analytics.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://tag.digitaltarget.ru/adcm.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/metrika/tag.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://websdk.appsflyer.com/?st=banners&", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "af_id=613d8563-c9dd-4ea4-9243-cd72e63ee6e3-p",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://sync.1dmp.io/pixel.gif?cid=ae1a1633-15da-47e0-a3a4-41fb59d62f2b&brid=07cef8a7-9b65-42fe-b55c-b758df5fa5cd&pid=w&uid=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0&gtmcb=528704320", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "uid=cdf98221-4809-11ed-acfd-901b0e8b2a6e",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/divcalendar/v1/dividend/NL0009805522", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/news/emitentnews?newsCount=9&securCode=YNDX&classCode=TQBR", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/v1/forecast/consensus/0?ticker=TQBR%7CYNDX", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/technical_analysis/v1/Article/GetByInstrument/YNDX", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/configs/v1?widgets=QuotesWidget", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://www.google-analytics.com/collect", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "v=1&_v=j98&a=167934326&t=pageview&_s=1&dl=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&ul=ru-ru&de=UTF-8&dt=%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sd=24-bit&sr=1920x1080&vp=1271x969&je=0&_u=QACAAEABAAAAAAAAI~&jid=&gjid=&cid=986744090.1639163756&tid=UA-4674261-2&_gid=2108351062.1666384778&gtm=2wgaj0M84QXK&z=377910730",
  "method": "POST"
}); ;
fetch("https://bcs-express.ru/assets2/styles/7733.min.css?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/scripts/7733.min.js?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/watch/887074?wmode=7&page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&page-ref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&charset=utf-8&browser-info=pv%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afp%3A249%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A0%3Als%3A1373863452275%3Ahid%3A720340559%3Az%3A180%3Ai%3A20221022020900%3Aet%3A1666393740%3Ac%3A1%3Arn%3A770073081%3Arqn%3A55%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Ads%3A0%2C0%2C123%2C51%2C1%2C0%2C%2C7%2C0%2C%2C%2C%2C384%3Acpf%3A1%3Ans%3A1666393739559%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666393740%3At%3A%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&t=gdpr(14)clc(0-0-0)aw(1)rqnt(1)rqnl(1)ti(2)", {
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
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://tag.digitaltarget.ru/processor.js?i=854933601400664", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/watch/887074/1?page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&charset=utf-8&hittoken=1666393738_ec0acc3c06208394426dd4f002b6adb7150836e0e54e033b4cf79c2f87e1723e&browser-info=pa%3A1%3Aar%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afu%3A1%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A0%3Als%3A1373863452275%3Ahid%3A720340559%3Az%3A180%3Ai%3A20221022020900%3Aet%3A1666393740%3Ac%3A1%3Arn%3A636835660%3Arqn%3A56%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Acpf%3A1%3Ans%3A1666393739559%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666393740&t=gdpr(14)mc(p-1-ui-1)clc(0-0-0)lt(6800)aw(1)rqnt(2)rqnl(1)ti(2)", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "site-info=%7B%22__ym%22%3A%7B%22user_id%22%3A%22e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%22%7D%7D",
  "method": "POST"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=93660713238668.460778142518653&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:adcmjs_init%20cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=93660713238668.724486538518701&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs.ru/company-logos/yandex.svg", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "_ym_d=1644086518; _ym_uid=1644086518108212344",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/favicon.ico", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("chrome-extension://iekplbcabikbagobpmocbadaebhoekci/content/styles.css", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/runtime.dad4fc3720eb75cc6832.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/vendors.ae60bddd431f61b0d826.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.3582b5aee6fe5013e68a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/custom/styles.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/32.27d1f6a4564f13116070.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/39.7c122268b8118d2aaa59.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/63.1dcbc7aa3999df0c4e14.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/77.251aca00b6d789124aa9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/15.c3822fc777211ee8315c.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/30.d95a3f827655ae6f4d41.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/35.cdf3658f4055352d11fd.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/47.bd5957415fc28f83be44.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/57.7dbb2fa612975a074b3d.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/floating-toolbars.a42568ef140544275245.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/react.5c26d836993909a1b0b6.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/1.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/4.4ff9c577f4760401b8ac.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/8.451da7e139a77029afdd.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/9.efabbd82e0d48b89b9ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/23.d6e5c055df8f94e561a4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/24.5e10ad1f5bf480fb2b22.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/26.af909889ef61e3630cfc.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/43.da62deb6f4f1ddeea0b7.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/45.71eab448131944179f76.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/46.fc24c2c028c08753d55b.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/60.0b2b2d99a039b120fb25.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/64.c7c323e7fdf173702b72.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/69.ed35d12e9213121440b4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/0.3a5522db90c672e977eb.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/2.2db061cb0002d932bfba.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/12.19fddd1156a17841a7f3.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/14.f0c743fc89255ca1fdc0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/18.44a018fdf841b272e3c2.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/52.e9f9363307cf0f56bd9b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-bottom-toolbar.06ad0fcc06b649c280d0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/70.736727f897e2be517230.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-widget-gui.5650b2a3d8cef650fbe8.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/7.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/27.28593ed548e579e8b63d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/33.8dd04cdbdff54e865f75.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/59.3c85911ad1fb5ec78b74.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/67.61a74b077527e7385641.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/68.f0d6d87e38e67f352f9e.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/restricted-toolset.2bc02c414ab2f059164a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/44.7ec72ee1a8a8ef96dbc9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/75.17abe3e8dce352c1b3ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/38.f7058b17c9cf23a00b5b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/header-toolbar.7934fd007ac019e54467.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/symbols?symbol=YNDX&classcode=TQBR", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/72.c7dff1d5063ddf603a81.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/drawing-toolbar.3fe1c12b08f4d9eace86.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/study-pane-views.f4a2713441042362cb3a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%2337A6EF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%23FFFFFF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660916307&to=1666393801", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660916307&to=1666393801", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/40f9a03d174178efb12303caa9bc7cd8.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357752&to=1666393752", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357752&to=1666393752", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357762&to=1666393762", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357762&to=1666393762", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/scripts/971.min.js?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357772&to=1666393772", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357772&to=1666393772", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357782&to=1666393782", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357782&to=1666393782", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357792&to=1666393792", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357792&to=1666393792", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357802&to=1666393802", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357802&to=1666393802", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357812&to=1666393812", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357812&to=1666393812", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357822&to=1666393822", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357822&to=1666393822", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357832&to=1666393832", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357832&to=1666393832", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357842&to=1666393842", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357842&to=1666393842", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357852&to=1666393852", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357852&to=1666393852", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357862&to=1666393862", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357862&to=1666393862", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357872&to=1666393872", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357872&to=1666393872", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357882&to=1666393882", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357882&to=1666393882", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357892&to=1666393892", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357892&to=1666393892", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357902&to=1666393902", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357902&to=1666393902", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357912&to=1666393912", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357912&to=1666393912", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357922&to=1666393922", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357922&to=1666393922", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357932&to=1666393932", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357932&to=1666393932", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357942&to=1666393942", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357942&to=1666393942", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357952&to=1666393952", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357952&to=1666393952", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357962&to=1666393962", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357962&to=1666393962", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357972&to=1666393972", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357972&to=1666393972", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357982&to=1666393982", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357982&to=1666393982", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357992&to=1666393992", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666357992&to=1666393992", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358002&to=1666394002", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358002&to=1666394002", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358012&to=1666394012", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358012&to=1666394012", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358022&to=1666394022", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358022&to=1666394022", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358032&to=1666394032", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358032&to=1666394032", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358042&to=1666394042", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358042&to=1666394042", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358052&to=1666394052", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358052&to=1666394052", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358062&to=1666394062", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358062&to=1666394062", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358072&to=1666394072", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358072&to=1666394072", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358082&to=1666394082", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358082&to=1666394082", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358092&to=1666394092", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358092&to=1666394092", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358102&to=1666394102", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358102&to=1666394102", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358112&to=1666394112", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358112&to=1666394112", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358122&to=1666394122", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358122&to=1666394122", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358132&to=1666394132", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358132&to=1666394132", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358142&to=1666394142", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358142&to=1666394142", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358152&to=1666394152", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358152&to=1666394152", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358162&to=1666394162", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358162&to=1666394162", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358172&to=1666394172", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358172&to=1666394172", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358182&to=1666394182", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358182&to=1666394182", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358192&to=1666394192", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358192&to=1666394192", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358202&to=1666394202", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358202&to=1666394202", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358212&to=1666394212", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358212&to=1666394212", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358234&to=1666394234", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358234&to=1666394234", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358294&to=1666394294", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358294&to=1666394294", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358340&to=1666394340", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358340&to=1666394340", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358342&to=1666394342", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358342&to=1666394342", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358352&to=1666394352", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358352&to=1666394352", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358362&to=1666394362", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358362&to=1666394362", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358372&to=1666394372", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358372&to=1666394372", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358382&to=1666394382", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358382&to=1666394382", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358392&to=1666394392", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358392&to=1666394392", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358402&to=1666394402", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358402&to=1666394402", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358412&to=1666394412", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358412&to=1666394412", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358422&to=1666394422", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358422&to=1666394422", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358432&to=1666394432", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358432&to=1666394432", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358442&to=1666394442", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358442&to=1666394442", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Bold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Regular-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Semibold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/styles/quotes-item.min.css?v=xcyY95o8cE7Xb4BnKeFoOghxKzq7BMf8-rWp_7WFpuU", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://polyfill.io/v3/polyfill.min.js?features=es6%2Ces2017%2CIntersectionObserver%2CIntersectionObserverEntry%2Cfetch%2CResizeObserver", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/runtime.min.js?v=i5zg03rnFRrdE0cxTxDtC6w3jyWqGZ50wgkSJpE7_Ys", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/vendor.min.js?v=E7uV_riU80FaUrTLNNgpinagiIRwHr9rL7A3mGk_GmM", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/quotes-item.min.js?v=9IHQ6hrnFLifQZXbRbkQhIWvN_GeI7vaPCCGUJKg6W8", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.googletagmanager.com/gtm.js?id=GTM-M84QXK", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjMwMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBvcGFjaXR5PSIuMiIgZD0iTTAgMzE0LjF2LTE3NEMwIDYyLjc4IDYyLjY4LjEgMTQwIC4xaDIwMHYzMTRIMFoiIGZpbGw9InVybCgjYSkiLz48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSIwIiB5MT0iMjU3LjAwOSIgeDI9IjMwMS43NSIgeTI9IjI1Ny4wMDkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjQTlBM0U5Ii8+PHN0b3Agb2Zmc2V0PSIuOTAxIiBzdG9wLWNvbG9yPSIjQTlBM0U5IiBzdG9wLW9wYWNpdHk9IjAiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google-analytics.com/analytics.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://tag.digitaltarget.ru/adcm.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/metrika/tag.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://websdk.appsflyer.com/?st=banners&", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "af_id=613d8563-c9dd-4ea4-9243-cd72e63ee6e3-p",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://sync.1dmp.io/pixel.gif?cid=ae1a1633-15da-47e0-a3a4-41fb59d62f2b&brid=07cef8a7-9b65-42fe-b55c-b758df5fa5cd&pid=w&uid=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0&gtmcb=1374431504", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "uid=cdf98221-4809-11ed-acfd-901b0e8b2a6e",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/divcalendar/v1/dividend/NL0009805522", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/news/emitentnews?newsCount=9&securCode=YNDX&classCode=TQBR", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/v1/forecast/consensus/0?ticker=TQBR%7CYNDX", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/technical_analysis/v1/Article/GetByInstrument/YNDX", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/configs/v1?widgets=QuotesWidget", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/styles/7733.min.css?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/scripts/7733.min.js?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google-analytics.com/j/collect?v=1&_v=j98&a=1220668579&t=pageview&_s=1&dl=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&ul=ru-ru&de=UTF-8&dt=%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sd=24-bit&sr=1920x1080&vp=1271x969&je=0&_u=QACAAEABAAAAACAAI~&jid=363449608&gjid=483932291&cid=986744090.1639163756&tid=UA-4674261-2&_gid=2108351062.1666384778&_r=1&gtm=2wgaj0M84QXK&z=2010624264", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "text/plain",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "method": "POST"
}); ;
fetch("https://tag.digitaltarget.ru/processor.js?i=738561379650192", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/watch/887074?wmode=7&page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&page-ref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&charset=utf-8&browser-info=pv%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afp%3A1264%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A0%3Als%3A1373863452275%3Ahid%3A720211621%3Az%3A180%3Ai%3A20221022022044%3Aet%3A1666394445%3Ac%3A1%3Arn%3A665359212%3Arqn%3A57%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Ads%3A20%2C106%2C1030%2C42%2C1%2C0%2C%2C8%2C0%2C%2C%2C%2C1414%3Acpf%3A1%3Ans%3A1666394443072%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666394445%3At%3A%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&t=gdpr(14)clc(0-0-0)aw(1)rqnt(1)rqnl(1)ti(2)", {
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
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=363449608&gjid=483932291&_gid=2108351062.1666384778&_u=QACAAEAAAAAAACAAI~&z=27805714", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "text/plain",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "IDE=AHWqTUnG90D8vKZ6M_hjdqjmCq8U3s3VtxMuaUg9DJ37-JJV5PFHnIac2NAssXldxaQ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "method": "POST"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=559963447858729.701497677273902&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:adcmjs_init%20cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=559963447858729.178286809540527&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google.com/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=363449608&_u=QACAAEAAAAAAACAAI~&z=126300982", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "__Secure-3PSID=PQhsvVgSw8fYdB5KIFfg0MDnbroBQHw47B1z-7-x7bXSVR-0ml2vpKyCaavZM7-RfomeRQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AIKkIs1DH_5lJpd2OkwX4NgP392elABKwOBTuCJwI6yhw95EhnVWbGmGX5CbVDOf2jfnKYcPkg; NID=511=sM8cbyLlUMimZFIVpjUEF6GTHqR86uNiyY3tbgtQsDzn1dzMzW1C6DI2-Sfc5mq5LD93_99QJKjI0mPMBW0XVHf6-j1NH75J4EFNxf_eTIeSb424_1yS79houMGlEpW-3OzaFZHjZ9iVqhcnHLQAV80pRtt94JfXx1Uiw2lxj2osPcGC6zLXwkpLx9PaTEFLLYAOe2bZaNtHNMIphmMJuSKfL1hRTOhUKv5Ky6eX1WRZeJTs50WD6fn6HniVgQld_uQa_xuoDPOiEUen0PMjO5WWzZXryflMHJQpQML8QRS0yV6pDF3O9TO_bY4BNB39jmHlQe56iIPWjDMQLZexISe27J_WpSOgfEZ4YEO7Bcv_LMJosTqsTBgQxs5iGabAvdvKNe3AXUZokIeRuh4pqlvLkWmWbM9MZ7J8eNL1npo; 1P_JAR=2022-10-21-23",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google.ru/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=363449608&_u=QACAAEAAAAAAACAAI~&z=126300982", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "__Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSID=PwhsveYhxB--ikj6yrID0rLaCbx4dYKq_tkx_SCr7nxqlrpMDpVxcuZbdIYIi_e8lZTFnQ.; 1P_JAR=2022-10-21-22; NID=511=djAha0l0V5NGRxU1_T7Kg-4-gmL-Gan5n7sihqgVC8ydV5RBYVXmFTuC6Oa0uI2Bpr-dJp55snWDlzuQqlKa7FmilUEXvKtxZZo3MHOeNsrdz8HjCNR1OpTzriqw7p8fydDEX09DqWMAM5bHYcFPYYkvjXfQuy6JHO-dySZuSvTVzTZPmzfoN4fa5a7ciUl2GCFdmlqTviqpiZvA755K1PjBFs18153caKHGuc_19V5tzcWFIZf2SWjKVL-r7D3HqlzriQMaj9_vYFPkhgwyKw-dWPly8APpDfs623IaEyEA1ZZUflYUBr6cKLgSbQrEKZ_T3BVApv5tSKbjtprIKxlwVTfPyQRU1-XHRha_-Q",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/watch/887074/1?page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&charset=utf-8&hittoken=1666394443_ce086dcef743269d74c47131e6b91c7d64bd18848f6544c5b070f8bd0f788bd3&browser-info=pa%3A1%3Aar%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afu%3A1%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A0%3Als%3A1373863452275%3Ahid%3A720211621%3Az%3A180%3Ai%3A20221022022044%3Aet%3A1666394445%3Ac%3A1%3Arn%3A335012329%3Arqn%3A58%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Acpf%3A1%3Ans%3A1666394443072%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666394445&t=gdpr(14)mc(p-1-ui-1)clc(0-0-0)lt(8000)aw(1)rqnt(2)rqnl(1)ti(2)", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "site-info=%7B%22__ym%22%3A%7B%22user_id%22%3A%22e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%22%7D%7D",
  "method": "POST"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs.ru/company-logos/yandex.svg", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "_ym_d=1644086518; _ym_uid=1644086518108212344",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/runtime.dad4fc3720eb75cc6832.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/vendors.ae60bddd431f61b0d826.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.3582b5aee6fe5013e68a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("chrome-extension://iekplbcabikbagobpmocbadaebhoekci/content/styles.css", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/custom/styles.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/favicon.ico", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/32.27d1f6a4564f13116070.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/39.7c122268b8118d2aaa59.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/63.1dcbc7aa3999df0c4e14.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/77.251aca00b6d789124aa9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/15.c3822fc777211ee8315c.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/30.d95a3f827655ae6f4d41.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/35.cdf3658f4055352d11fd.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/47.bd5957415fc28f83be44.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/57.7dbb2fa612975a074b3d.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/floating-toolbars.a42568ef140544275245.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/react.5c26d836993909a1b0b6.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/1.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/4.4ff9c577f4760401b8ac.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/8.451da7e139a77029afdd.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/9.efabbd82e0d48b89b9ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/23.d6e5c055df8f94e561a4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/24.5e10ad1f5bf480fb2b22.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/26.af909889ef61e3630cfc.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/43.da62deb6f4f1ddeea0b7.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/45.71eab448131944179f76.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/46.fc24c2c028c08753d55b.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/60.0b2b2d99a039b120fb25.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/64.c7c323e7fdf173702b72.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/69.ed35d12e9213121440b4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/0.3a5522db90c672e977eb.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/2.2db061cb0002d932bfba.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/12.19fddd1156a17841a7f3.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/14.f0c743fc89255ca1fdc0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/18.44a018fdf841b272e3c2.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/52.e9f9363307cf0f56bd9b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-bottom-toolbar.06ad0fcc06b649c280d0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/70.736727f897e2be517230.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-widget-gui.5650b2a3d8cef650fbe8.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/7.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/27.28593ed548e579e8b63d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/33.8dd04cdbdff54e865f75.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/59.3c85911ad1fb5ec78b74.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/67.61a74b077527e7385641.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/68.f0d6d87e38e67f352f9e.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/restricted-toolset.2bc02c414ab2f059164a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/44.7ec72ee1a8a8ef96dbc9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/75.17abe3e8dce352c1b3ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/38.f7058b17c9cf23a00b5b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/header-toolbar.7934fd007ac019e54467.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/symbols?symbol=YNDX&classcode=TQBR", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/72.c7dff1d5063ddf603a81.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/drawing-toolbar.3fe1c12b08f4d9eace86.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/study-pane-views.f4a2713441042362cb3a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%2337A6EF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%23FFFFFF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660917011&to=1666394505", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660917011&to=1666394505", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/40f9a03d174178efb12303caa9bc7cd8.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358456&to=1666394456", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358456&to=1666394456", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358466&to=1666394466", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358466&to=1666394466", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358476&to=1666394476", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358476&to=1666394476", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/83.9cb26800ae66a17fccc8.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-event-hint.a5bbf042a6ae27521744.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358486&to=1666394486", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358486&to=1666394486", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358496&to=1666394496", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358496&to=1666394496", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358506&to=1666394506", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358506&to=1666394506", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358516&to=1666394516", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358516&to=1666394516", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358526&to=1666394526", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358526&to=1666394526", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358536&to=1666394536", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358536&to=1666394536", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358546&to=1666394546", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358546&to=1666394546", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358556&to=1666394556", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358556&to=1666394556", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358566&to=1666394566", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358566&to=1666394566", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358576&to=1666394576", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358576&to=1666394576", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358586&to=1666394586", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358586&to=1666394586", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358596&to=1666394596", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358596&to=1666394596", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1659950795&to=1660917010", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1659950795&to=1660917010", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1656609561&to=1659950794", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1656609561&to=1659950794", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1655787946&to=1656609560", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1655787946&to=1656609560", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1652693196&to=1655787945", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1652693196&to=1655787945", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358606&to=1666394606", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358606&to=1666394606", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358616&to=1666394616", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358616&to=1666394616", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1651008895&to=1652693195", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1651008895&to=1652693195", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1647448563&to=1651008894", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1647448563&to=1651008894", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1647037756&to=1647448562", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1647037756&to=1647448562", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1646626948&to=1647037755", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1646626948&to=1647037755", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1646216141&to=1646626947", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1646216141&to=1646626947", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645805334&to=1646216140", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645805334&to=1646216140", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645394526&to=1645805333", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645394526&to=1645805333", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645038493&to=1645394525", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1645038493&to=1645394525", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358626&to=1666394626", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358626&to=1666394626", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358636&to=1666394636", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358636&to=1666394636", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358646&to=1666394646", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358646&to=1666394646", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358656&to=1666394656", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358656&to=1666394656", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1632266664&to=1666394724", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1632266664&to=1666394724", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1665530674&to=1666394674", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1665530674&to=1666394674", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1630970675&to=1632266663", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1630970675&to=1632266663", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1630970675&to=1666394735", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1630970675&to=1666394735", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1611962675&to=1630970674", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1611962675&to=1630970674", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1611962675&to=1666394735", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1611962675&to=1666394735", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1606433076&to=1611962674", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1606433076&to=1611962674", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1604445876&to=1606433075", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=D&from=1604445876&to=1606433075", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Bold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Regular-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/fonts/Graphik-Semibold-Web.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/styles/quotes-item.min.css?v=xcyY95o8cE7Xb4BnKeFoOghxKzq7BMf8-rWp_7WFpuU", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://polyfill.io/v3/polyfill.min.js?features=es6%2Ces2017%2CIntersectionObserver%2CIntersectionObserverEntry%2Cfetch%2CResizeObserver", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/runtime.min.js?v=i5zg03rnFRrdE0cxTxDtC6w3jyWqGZ50wgkSJpE7_Ys", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/vendor.min.js?v=E7uV_riU80FaUrTLNNgpinagiIRwHr9rL7A3mGk_GmM", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/assets2/scripts/quotes-item.min.js?v=9IHQ6hrnFLifQZXbRbkQhIWvN_GeI7vaPCCGUJKg6W8", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.googletagmanager.com/gtm.js?id=GTM-M84QXK", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjMwMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBvcGFjaXR5PSIuMiIgZD0iTTAgMzE0LjF2LTE3NEMwIDYyLjc4IDYyLjY4LjEgMTQwIC4xaDIwMHYzMTRIMFoiIGZpbGw9InVybCgjYSkiLz48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSIwIiB5MT0iMjU3LjAwOSIgeDI9IjMwMS43NSIgeTI9IjI1Ny4wMDkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjQTlBM0U5Ii8+PHN0b3Agb2Zmc2V0PSIuOTAxIiBzdG9wLWNvbG9yPSIjQTlBM0U5IiBzdG9wLW9wYWNpdHk9IjAiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google-analytics.com/analytics.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://tag.digitaltarget.ru/adcm.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://mc.yandex.ru/metrika/tag.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://websdk.appsflyer.com/?st=banners&", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "af_id=613d8563-c9dd-4ea4-9243-cd72e63ee6e3-p",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://sync.1dmp.io/pixel.gif?cid=ae1a1633-15da-47e0-a3a4-41fb59d62f2b&brid=07cef8a7-9b65-42fe-b55c-b758df5fa5cd&pid=w&uid=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0&gtmcb=1107076807", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "uid=cdf98221-4809-11ed-acfd-901b0e8b2a6e",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://tag.digitaltarget.ru/processor.js?i=292623083581646", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/divcalendar/v1/dividend/NL0009805522", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/news/emitentnews?newsCount=9&securCode=YNDX&classCode=TQBR", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/webapi/api/v1/forecast/consensus/0?ticker=TQBR%7CYNDX", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/technical_analysis/v1/Article/GetByInstrument/YNDX", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/community/v1/questionanalytics?limit=10&tag=yndx", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/configs/v1?widgets=QuotesWidget", {
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
    "sec-fetch-site": "same-origin",
    "ticket": "",
    "token": "",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/news_api/v1/investmentIea/emitent?author=0&limit=10&classCode=TQBR&secureCode=YNDX", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://my.broker.ru/express/api/v1/newsfeed/posts?take=5&instrument=YNDX%3BTQBR", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/styles/7733.min.css?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/scripts/7733.min.js?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=617504353044589.316387207344893&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:adcmjs_init%20cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://dmg.digitaltarget.ru/1/6578/i/i?i=617504353044589.308870104944006&pref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&c=xdua:duTjaztQjLPsxLM80o_gS976.xps:xpszuR4tnSqgjpGoAOJoyqcyL.xga:GA1_2_986744090_1639163756.xgid:GA1_2_2108351062_1666384778.dn:bcs_express__ru.adcm:hit.tg:cuid_e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%20adcmjs_noorient", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "viuserid=SpQy3yYJ9tRVOvX7apJZ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google-analytics.com/j/collect?v=1&_v=j98&a=1695296981&t=pageview&_s=1&dl=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&ul=ru-ru&de=UTF-8&dt=%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sd=24-bit&sr=1920x1080&vp=1271x969&je=0&_u=QACAAEABAAAAACAAI~&jid=1527446322&gjid=1898543005&cid=986744090.1639163756&tid=UA-4674261-2&_gid=2108351062.1666384778&_r=1&gtm=2wgaj0M84QXK&z=766301407", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "text/plain",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "",
  "method": "POST"
}); ;
fetch("https://mc.yandex.ru/watch/887074?wmode=7&page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&page-ref=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki&charset=utf-8&browser-info=pv%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afp%3A448%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A0%3Als%3A1373863452275%3Ahid%3A343205378%3Az%3A180%3Ai%3A20221022022436%3Aet%3A1666394677%3Ac%3A1%3Arn%3A465127468%3Arqn%3A59%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Ads%3A14%2C108%2C122%2C43%2C1%2C0%2C%2C17%2C0%2C%2C%2C%2C728%3Acpf%3A1%3Ans%3A1666394676132%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666394677%3At%3A%D0%90%D0%BA%D1%86%D0%B8%D0%B8%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%3A%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9%20Yandex%20%D0%BD%D0%B0%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%2C%20%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%20YNDX%20%D0%B2%20%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8%20(%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD)%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&t=gdpr(14)clc(0-0-0)aw(1)rqnt(1)rqnl(1)ti(2)", {
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
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=1527446322&gjid=1898543005&_gid=2108351062.1666384778&_u=QACAAEAAAAAAACAAI~&z=1856247944", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "text/plain",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "IDE=AHWqTUnG90D8vKZ6M_hjdqjmCq8U3s3VtxMuaUg9DJ37-JJV5PFHnIac2NAssXldxaQ",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "",
  "method": "POST"
}); ;
fetch("https://mc.yandex.ru/watch/887074/1?page-url=https%3A%2F%2Fbcs-express.ru%2Fkotirovki-i-grafiki%2Fyndx&charset=utf-8&hittoken=1666394675_65538540d2ea85128719b1965836db3196a182fafe5510ac04e8c6434ee647c7&browser-info=pa%3A1%3Aar%3A1%3Agdpr%3A14%3Avf%3Akqp6gvxtrlkq3u3woc7b0%3Afu%3A1%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A912%3Acn%3A1%3Adp%3A1%3Als%3A1373863452275%3Ahid%3A343205378%3Az%3A180%3Ai%3A20221022022436%3Aet%3A1666394677%3Ac%3A1%3Arn%3A900439119%3Arqn%3A60%3Au%3A1607113204822541148%3Aw%3A1271x969%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Acpf%3A1%3Ans%3A1666394676132%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1666394677&t=gdpr(14)mc(p-1-ui-1)clc(0-0-0)lt(12800)aw(1)rqnt(2)rqnl(1)ti(2)", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "cookie": "yandex_login=markov.ilya@mail.ru; Session_id=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1|1630156653.0.2|3:10258637.83653._hvmlwFET4gQtMlwuT8T_IzmUN8; sessionid2=3:1663883422.5.0.1660245217737:o_ihXw:2b.1.2:1.499:1|1630156653.0.2|3:10258637.977720.fakesign0000000000000000000; yabs-sid=1349017071666368133; yandexuid=1543127351665486149; yuidss=1543127351665486149; yp=1666458317.yu.5114335311666028642; i=ybZWzrBm7G0qVQEmmV6PMQLOusj52zc9B+/aZUjIh49MyKBZPwa1A86v0sajOJwmiUKYXCue4WZSV1h2DJhwQxqLAN0=; ymex=1668963917.oyu.5114335311666028642#1981388642.yrts.1666028642#1981731917.yrtsi.1666371917",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "site-info=%7B%22__ym%22%3A%7B%22user_id%22%3A%22e636a0a9-2c9d-4799-aa96-46d7e75d2fd0%22%7D%7D",
  "method": "POST"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google.com/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=1527446322&_u=QACAAEAAAAAAACAAI~&z=427232782", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "__Secure-3PSID=PQhsvVgSw8fYdB5KIFfg0MDnbroBQHw47B1z-7-x7bXSVR-0ml2vpKyCaavZM7-RfomeRQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AIKkIs1DH_5lJpd2OkwX4NgP392elABKwOBTuCJwI6yhw95EhnVWbGmGX5CbVDOf2jfnKYcPkg; NID=511=sM8cbyLlUMimZFIVpjUEF6GTHqR86uNiyY3tbgtQsDzn1dzMzW1C6DI2-Sfc5mq5LD93_99QJKjI0mPMBW0XVHf6-j1NH75J4EFNxf_eTIeSb424_1yS79houMGlEpW-3OzaFZHjZ9iVqhcnHLQAV80pRtt94JfXx1Uiw2lxj2osPcGC6zLXwkpLx9PaTEFLLYAOe2bZaNtHNMIphmMJuSKfL1hRTOhUKv5Ky6eX1WRZeJTs50WD6fn6HniVgQld_uQa_xuoDPOiEUen0PMjO5WWzZXryflMHJQpQML8QRS0yV6pDF3O9TO_bY4BNB39jmHlQe56iIPWjDMQLZexISe27J_WpSOgfEZ4YEO7Bcv_LMJosTqsTBgQxs5iGabAvdvKNe3AXUZokIeRuh4pqlvLkWmWbM9MZ7J8eNL1npo; 1P_JAR=2022-10-21-23",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google.ru/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j98&tid=UA-4674261-2&cid=986744090.1639163756&jid=1527446322&_u=QACAAEAAAAAAACAAI~&z=427232782", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEIlKHLAQjhu8wBCPK8zAEIxuHMAQib6swB",
    "cookie": "__Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSID=PwhsveYhxB--ikj6yrID0rLaCbx4dYKq_tkx_SCr7nxqlrpMDpVxcuZbdIYIi_e8lZTFnQ.; 1P_JAR=2022-10-21-22; NID=511=djAha0l0V5NGRxU1_T7Kg-4-gmL-Gan5n7sihqgVC8ydV5RBYVXmFTuC6Oa0uI2Bpr-dJp55snWDlzuQqlKa7FmilUEXvKtxZZo3MHOeNsrdz8HjCNR1OpTzriqw7p8fydDEX09DqWMAM5bHYcFPYYkvjXfQuy6JHO-dySZuSvTVzTZPmzfoN4fa5a7ciUl2GCFdmlqTviqpiZvA755K1PjBFs18153caKHGuc_19V5tzcWFIZf2SWjKVL-r7D3HqlzriQMaj9_vYFPkhgwyKw-dWPly8APpDfs623IaEyEA1ZZUflYUBr6cKLgSbQrEKZ_T3BVApv5tSKbjtprIKxlwVTfPyQRU1-XHRha_-Q",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs.ru/company-logos/yandex.svg", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "cookie": "_ym_d=1644086518; _ym_uid=1644086518108212344",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("chrome-extension://iekplbcabikbagobpmocbadaebhoekci/content/styles.css", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/runtime.dad4fc3720eb75cc6832.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/vendors.ae60bddd431f61b0d826.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.3582b5aee6fe5013e68a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/custom/styles.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://cdn.bcs-express.ru/article-head/7181.jpg", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/32.27d1f6a4564f13116070.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/39.7c122268b8118d2aaa59.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/63.1dcbc7aa3999df0c4e14.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/77.251aca00b6d789124aa9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/15.c3822fc777211ee8315c.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/30.d95a3f827655ae6f4d41.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/35.cdf3658f4055352d11fd.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/47.bd5957415fc28f83be44.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/57.7dbb2fa612975a074b3d.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/floating-toolbars.a42568ef140544275245.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/react.5c26d836993909a1b0b6.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/1.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/4.4ff9c577f4760401b8ac.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/8.451da7e139a77029afdd.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/9.efabbd82e0d48b89b9ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/23.d6e5c055df8f94e561a4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/24.5e10ad1f5bf480fb2b22.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/26.af909889ef61e3630cfc.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/43.da62deb6f4f1ddeea0b7.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/45.71eab448131944179f76.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/46.fc24c2c028c08753d55b.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/60.0b2b2d99a039b120fb25.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/64.c7c323e7fdf173702b72.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/69.ed35d12e9213121440b4.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/0.3a5522db90c672e977eb.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/2.2db061cb0002d932bfba.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/12.19fddd1156a17841a7f3.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/14.f0c743fc89255ca1fdc0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/18.44a018fdf841b272e3c2.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/52.e9f9363307cf0f56bd9b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-bottom-toolbar.06ad0fcc06b649c280d0.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/70.736727f897e2be517230.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-widget-gui.5650b2a3d8cef650fbe8.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/7.92647ec0a7beb8b2898d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/27.28593ed548e579e8b63d.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/33.8dd04cdbdff54e865f75.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/59.3c85911ad1fb5ec78b74.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/67.61a74b077527e7385641.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/68.f0d6d87e38e67f352f9e.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/restricted-toolset.2bc02c414ab2f059164a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/44.7ec72ee1a8a8ef96dbc9.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/75.17abe3e8dce352c1b3ab.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/38.f7058b17c9cf23a00b5b.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/header-toolbar.7934fd007ac019e54467.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/symbols?symbol=YNDX&classcode=TQBR", {
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
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/72.c7dff1d5063ddf603a81.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/drawing-toolbar.3fe1c12b08f4d9eace86.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/study-pane-views.f4a2713441042362cb3a.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/favicon.ico", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%2337A6EF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2022%2013%22%20width%3D%2222%22%20height%3D%2213%22%3E%3Cpath%20fill%3D%22%23FFFFFF%22%20fill-rule%3D%22nonzero%22%20d%3D%22M19.354%204.932c.379.55.611%201.207.642%201.918A3.007%203.007%200%200%201%2022%209.686a3.003%203.003%200%200%201-3%203.006H4a3.983%203.983%200%200%201-2.814-1.16l6.363-5.048a1.657%201.657%200%200%200%201.495.037l3.034%202.66a1.672%201.672%200%200%200%201.589%202.175%201.668%201.668%200%200%200%201.552-2.28l4.135-4.144zm-.942-.945L14.276%208.13a1.66%201.66%200%200%200-1.32.044l-3.034-2.66A1.672%201.672%200%200%200%208.333%203.34a1.668%201.668%200%200%200-1.611%202.097l-6.316%205.01A3.999%203.999%200%200%201%200%208.683a4.004%204.004%200%200%201%204.041-4.008A5.338%205.338%200%200%201%209.333%200a5.337%205.337%200%200%201%205.124%203.857%203.644%203.644%200%200%201%201.876-.517c.772%200%201.488.239%202.079.647z%22%2F%3E%3C%2Fsvg%3E", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660917244&to=1666394738", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1660917244&to=1666394738", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/40f9a03d174178efb12303caa9bc7cd8.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/bundles/library.848bbe7df0cc8e3d6bf5.css",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/83.9cb26800ae66a17fccc8.css", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://bcs-express.ru/assets2/charting_library/bundles/chart-event-hint.a5bbf042a6ae27521744.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/assets2/charting_library/ru-tv-chart.c3634edc.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1659950870&to=1660917243", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1659950870&to=1660917243", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1657828365&to=1659950869", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1657828365&to=1659950869", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358689&to=1666394689", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358689&to=1666394689", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358699&to=1666394699", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358699&to=1666394699", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358709&to=1666394709", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358709&to=1666394709", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358719&to=1666394719", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358719&to=1666394719", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358729&to=1666394729", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358729&to=1666394729", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://bcs-express.ru/assets2/scripts/971.min.js?1e9a7d1ad44b122da0a7", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ym_uid=1607113204822541148; _ga=GA1.2.986744090.1639163756; bcs_user_id=e636a0a9-2c9d-4799-aa96-46d7e75d2fd0; _a_d3t6sf=duTjaztQjLPsxLM80o_gS976; spid=1656344494536_50cd0ba478f72452199ab63c5bfc0a1e_vgae782jk08a450w; _ym_d=1663801923; _gid=GA1.2.2108351062.1666384778; _ym_isad=2; _gat_UA-4674261-2=1",
    "Referer": "https://bcs-express.ru/kotirovki-i-grafiki/yndx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358739&to=1666394739", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358739&to=1666394739", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358749&to=1666394749", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358749&to=1666394749", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358759&to=1666394759", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358759&to=1666394759", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358769&to=1666394769", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358769&to=1666394769", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358779&to=1666394779", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358779&to=1666394779", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358789&to=1666394789", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358789&to=1666394789", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358799&to=1666394799", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358799&to=1666394799", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358809&to=1666394809", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358809&to=1666394809", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358819&to=1666394819", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358819&to=1666394819", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358829&to=1666394829", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358829&to=1666394829", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358839&to=1666394839", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358839&to=1666394839", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358849&to=1666394849", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358849&to=1666394849", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358859&to=1666394859", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358859&to=1666394859", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358869&to=1666394869", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358869&to=1666394869", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358879&to=1666394879", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358879&to=1666394879", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=TQBR%7CYNDX&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/info?instruments=INDX%7CIMOEX&instruments=FEX%7CS%26P500&instruments=CETS%7CUSD000UTSTOM&instruments=CETS%7CEUR_RUB__TOM&instruments=CETS%7CEURUSD000TOM&instruments=FEG%7CBRENT&inOrderArray=true", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358889&to=1666394889", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358889&to=1666394889", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358899&to=1666394899", {
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
  "body": null,
  "method": "GET"
}); ;
fetch("https://api.bcs.ru/udfdatafeed/v1/history?symbol=YNDX&classcode=TQBR&resolution=60&from=1666358899&to=1666394899", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://bcs-express.ru/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "OPTIONS"
});
})
print(price.status_code)
print(p)