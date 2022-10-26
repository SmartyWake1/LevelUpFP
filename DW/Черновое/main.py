import requests
response = requests.get("https://bcs-express.ru/kotirovki-i-grafiki/yndx")
print(response.json)
print(response.text)
fetch("https://www.youtube.com/", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "service-worker-navigation-preload": "true",
    "upgrade-insecure-requests": "1",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1"
  },
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "service-worker-navigation-preload": "true",
    "upgrade-insecure-requests": "1"
  },
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/youtubei/v1/att/get?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "SAPISIDHASH 1666392542_67401f0d5624eead5c253668d233dac387b7b28e",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "x-goog-authuser": "0",
    "x-goog-visitor-id": "CgtGM3NPWHp6UWZyQSjaw8yaBg%3D%3D",
    "x-origin": "https://www.youtube.com",
    "x-youtube-bootstrap-logged-in": "false",
    "x-youtube-client-name": "1",
    "x-youtube-client-version": "2.20221021.00.00",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"context\":{\"client\":{\"hl\":\"ru\",\"gl\":\"RU\",\"remoteHost\":\"95.161.248.163\",\"deviceMake\":\"\",\"deviceModel\":\"\",\"visitorData\":\"CgtGM3NPWHp6UWZyQSjaw8yaBg%3D%3D\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36,gzip(gfe)\",\"clientName\":\"WEB\",\"clientVersion\":\"2.20221021.00.00\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"originalUrl\":\"https://www.youtube.com/\",\"platform\":\"DESKTOP\",\"clientFormFactor\":\"UNKNOWN_FORM_FACTOR\",\"configInfo\":{\"appInstallData\":\"CNrDzJoGEKjUrgUQuIuuBRDiua4FELKI_hIQ28quBRCZxq4FEOrKrgUQm8quBRDpjf4SEOrVrgUQ1IOuBRCJj_4SENi-rQUQkfj8Eg%3D%3D\"},\"timeZone\":\"Etc/GMT-3\",\"browserName\":\"Chrome\",\"browserVersion\":\"106.0.0.0\",\"acceptHeader\":\"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\",\"deviceExperimentId\":\"CgtrOWtYdzNQZm1JNBDaw8yaBg%3D%3D\",\"screenWidthPoints\":1501,\"screenHeightPoints\":969,\"screenPixelDensity\":1,\"screenDensityFloat\":1,\"utcOffsetMinutes\":180,\"userInterfaceTheme\":\"USER_INTERFACE_THEME_LIGHT\",\"connectionType\":\"CONN_CELLULAR_4G\",\"memoryTotalKbytes\":\"8000000\",\"mainAppWebInfo\":{\"graftUrl\":\"https://www.youtube.com/\",\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\",\"isWebNativeShareAvailable\":true},\"playerType\":\"UNIPLAYER\",\"tvAppInfo\":{\"livingRoomAppMode\":\"LIVING_ROOM_APP_MODE_UNSPECIFIED\"}},\"user\":{\"lockedSafetyMode\":false},\"request\":{\"useSsl\":true,\"internalExperimentFlags\":[],\"consistencyTokenJars\":[]},\"adSignalsInfo\":{\"params\":[{\"key\":\"dt\",\"value\":\"1666392541132\"},{\"key\":\"flash\",\"value\":\"0\"},{\"key\":\"frm\",\"value\":\"0\"},{\"key\":\"u_tz\",\"value\":\"180\"},{\"key\":\"u_his\",\"value\":\"2\"},{\"key\":\"u_h\",\"value\":\"1080\"},{\"key\":\"u_w\",\"value\":\"1920\"},{\"key\":\"u_ah\",\"value\":\"1040\"},{\"key\":\"u_aw\",\"value\":\"1920\"},{\"key\":\"u_cd\",\"value\":\"24\"},{\"key\":\"bc\",\"value\":\"31\"},{\"key\":\"bih\",\"value\":\"969\"},{\"key\":\"biw\",\"value\":\"1485\"},{\"key\":\"brdim\",\"value\":\"0,0,0,0,1920,0,1920,1040,1501,969\"},{\"key\":\"vis\",\"value\":\"1\"},{\"key\":\"wgl\",\"value\":\"true\"},{\"key\":\"ca_type\",\"value\":\"image\"}],\"bid\":\"ANyPxKoBiRuo2Hakl2JDFnChLNfh9AS1BIQT4_64_tvlLo3K84G61EOKDUU-pWFC-2kIa6OrsquiuOarNgeZfDtlmZPvEPzZQQ\"}},\"engagementType\":\"ENGAGEMENT_TYPE_PLAYBACK\",\"ids\":[{\"playbackId\":{\"cpn\":\"lG_fFNK6PLkdvuul\"}}]}",
  "method": "POST"
}); ;
fetch("https://www.google.com/js/th/4tfOQvN7jkOjl-XJptbJRMDKonuctR4YaRgLNEs4SL8.js", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "__Secure-3PSID=PQhsvVgSw8fYdB5KIFfg0MDnbroBQHw47B1z-7-x7bXSVR-0ml2vpKyCaavZM7-RfomeRQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AIKkIs1DH_5lJpd2OkwX4NgP392elABKwOBTuCJwI6yhw95EhnVWbGmGX5CbVDOf2jfnKYcPkg; 1P_JAR=2022-10-21-22; NID=511=sM8cbyLlUMimZFIVpjUEF6GTHqR86uNiyY3tbgtQsDzn1dzMzW1C6DI2-Sfc5mq5LD93_99QJKjI0mPMBW0XVHf6-j1NH75J4EFNxf_eTIeSb424_1yS79houMGlEpW-3OzaFZHjZ9iVqhcnHLQAV80pRtt94JfXx1Uiw2lxj2osPcGC6zLXwkpLx9PaTEFLLYAOe2bZaNtHNMIphmMJuSKfL1hRTOhUKv5Ky6eX1WRZeJTs50WD6fn6HniVgQld_uQa_xuoDPOiEUen0PMjO5WWzZXryflMHJQpQML8QRS0yV6pDF3O9TO_bY4BNB39jmHlQe56iIPWjDMQLZexISe27J_WpSOgfEZ4YEO7Bcv_LMJosTqsTBgQxs5iGabAvdvKNe3AXUZokIeRuh4pqlvLkWmWbM9MZ7J8eNL1npo",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/generate_204?MftatQ", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-searchbox.vflset/www-searchbox.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("data:image/gif;base64,R0lGODlhEwALAKECAAAAABISEv///////yH5BAEKAAIALAAAAAATAAsAAAIdDI6pZ+suQJyy0ocV3bbm33EcCArmiUYk1qxAUAAAOw==", {
  "referrer": "",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.gstatic.com/inputtools/images/tia.png", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.googleapis.com/css?family=Roboto:300italic,400italic,500italic,700italic", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.googleapis.com/css?family=Roboto+Mono:400", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/youtubei/v1/log_event?alt=json&key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "SAPISIDHASH 1666392551_6803f555f424f57fbb97488323ef166f86c638c7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "x-goog-authuser": "",
    "x-goog-request-time": "1666392551390",
    "x-goog-visitor-id": "CgtGM3NPWHp6UWZyQSjaw8yaBg%3D%3D",
    "x-origin": "https://www.youtube.com",
    "x-youtube-ad-signals": "dt=1666392539831&flash=0&frm&u_tz=180&u_his=2&u_h=1080&u_w=1920&u_ah=1040&u_aw=1920&u_cd=24&bc=31&bih=969&biw=1485&brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1040%2C1501%2C969&vis=1&wgl=true&ca_type=image&bid=ANyPxKoBiRuo2Hakl2JDFnChLNfh9AS1BIQT4_64_tvlLo3K84G61EOKDUU-pWFC-2kIa6OrsquiuOarNgeZfDtlmZPvEPzZQQ",
    "x-youtube-client-name": "1",
    "x-youtube-client-version": "2.20221021.00.00",
    "x-youtube-device": "cbr=Chrome&cbrver=106.0.0.0&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0&cplatform=DESKTOP",
    "x-youtube-page-cl": "482690998",
    "x-youtube-page-label": "youtube.desktop.web_20221021_00_RC00",
    "x-youtube-time-zone": "Etc/GMT-3",
    "x-youtube-utc-offset": "180",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"context\":{\"client\":{\"hl\":\"ru\",\"gl\":\"RU\",\"clientName\":1,\"clientVersion\":\"2.20221021.00.00\",\"configInfo\":{\"appInstallData\":\"CNrDzJoGEKjUrgUQuIuuBRDiua4FELKI_hIQ28quBRCZxq4FEOrKrgUQm8quBRDpjf4SEOrVrgUQ1IOuBRCJj_4SENi-rQUQkfj8Eg%3D%3D\"},\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36\",\"mainAppWebInfo\":{\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\"},\"memoryTotalKbytes\":\"8000000\",\"connectionType\":\"CONN_CELLULAR_4G\",\"browserName\":\"Chrome\",\"browserVersion\":\"106.0.0.0\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"platform\":\"DESKTOP\"}},\"events\":[{\"eventTimeMs\":1666392540966,\"latencyActionTicked\":{\"tickName\":\"gpe\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"1125\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CBMQ04AEIhMIrOTy-rPy-gIVJMZPCB29NwYX\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAwQ5isYAyITCKzk8vqz8voCFSTGTwgdvTcGFw==\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAoQ5isYBCITCKzk8vqz8voCFSTGTwgdvTcGFw==\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAYQ5isYBSITCKzk8vqz8voCFSTGTwgdvTcGFw==\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CBIQv54JGAAiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CBEQp4EJGAEiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CBAQnOQDGAIiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CA8QpoEJGAMiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CA4QpIEJGAQiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CA0QqoEJGAUiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAsQtSwYACITCKzk8vqz8voCFSTGTwgdvTcGFw==\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAkQ4sUCGAAiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAgQ48UCGAEiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541010,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CAcQ4MUCGAIiEwis5PL6s_L6AhUkxk8IHb03Bhc=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1168\"}},{\"eventTimeMs\":1666392541045,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":110509,\"veCounter\":11},{\"veType\":110510,\"veCounter\":12}]},\"context\":{\"lastActivityMs\":\"1203\"}},{\"eventTimeMs\":1666392541049,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":115994,\"veCounter\":1}]},\"context\":{\"lastActivityMs\":\"1207\"}},{\"eventTimeMs\":1666392541049,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":115993,\"veCounter\":2}]},\"context\":{\"lastActivityMs\":\"1207\"}},{\"eventTimeMs\":1666392541087,\"adsClientStateChange\":{\"adsClientEvent\":{\"eventType\":\"ADS_CLIENT_EVENT_TYPE_OPPORTUNITY_RECEIVED\",\"eventOrder\":1,\"adClientData\":{\"opportunityData\":{\"opportunityType\":\"OPPORTUNITY_TYPE_ORGANIC_BROWSE_RESPONSE_RECEIVED\"}}}},\"context\":{\"lastActivityMs\":\"1245\"}},{\"eventTimeMs\":1666392541087,\"adsClientStateChange\":{\"adsClientEvent\":{\"eventType\":\"ADS_CLIENT_EVENT_TYPE_OPPORTUNITY_PROCESSED\",\"eventOrder\":2,\"adClientData\":{\"opportunityData\":{\"opportunityType\":\"OPPORTUNITY_TYPE_ORGANIC_BROWSE_RESPONSE_RECEIVED\"}}}},\"context\":{\"lastActivityMs\":\"1246\"}},{\"eventTimeMs\":1666392539537,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/network.vflset/network.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539536,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-onepick.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539535,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-main-desktop-home-page-skeleton.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539534,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.UrU5vkUWQCM.L.B1.O/am=AAE/d=0/br=1/rs=AGKMywEbyb0j4PcxSqqEUJ0-d7GCQna4fg\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539533,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/spf.vflset/spf.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539532,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-tampering.vflset/www-tampering.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539531,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-i18n-constants-ru_RU.vflset/www-i18n-constants.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539529,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/scheduler.vflset/scheduler.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539505,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/intersection-observer.min.vflset/intersection-observer.min.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539504,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/webcomponents-sd.vflset/webcomponents-sd.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539500,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/custom-elements-es5-adapter.vflset/custom-elements-es5-adapter.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539499,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/desktop_polymer.vflset/desktop_polymer.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392539498,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/web-animations-next-lite.min.vflset/web-animations-next-lite.min.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392303148,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/favicon.ico\",\"cacheHit\":false,\"currentAppBundleTimestampSec\":\"1666376153\",\"appBundleVersionDiffCount\":-1},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392051792,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-main-desktop-player-skeleton.css\",\"cacheHit\":false,\"currentAppBundleTimestampSec\":\"1666376153\",\"appBundleVersionDiffCount\":-1},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392051782,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.UrU5vkUWQCM.L.B1.O/am=AAE/d=0/br=1/rs=AGKMywEbyb0j4PcxSqqEUJ0-d7GCQna4fg\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392051781,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-onepick.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392051780,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-main-desktop-watch-page-skeleton.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392046157,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/www-player.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392017443,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/ru_RU/embed.js\",\"cacheHit\":false,\"currentAppBundleTimestampSec\":\"1666376153\",\"appBundleVersionDiffCount\":-1},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392017415,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/ru_RU/remote.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392017259,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/fetch-polyfill.vflset/fetch-polyfill.js\",\"cacheHit\":false,\"currentAppBundleTimestampSec\":\"1666376153\",\"appBundleVersionDiffCount\":-1},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392017258,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/www-embed-player.vflset/www-embed-player.js\",\"cacheHit\":false,\"currentAppBundleTimestampSec\":\"1666376153\",\"appBundleVersionDiffCount\":-1},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392017250,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/www-player.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666391332731,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-searchbox.vflset/www-searchbox.js\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666387441831,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/player/24c6f8bd/www-player.css\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666387441336,\"appShellAssetLoadReport\":{\"assetPath\":\"https://www.youtube.com/s/desktop/41dc17d1/img/favicon.ico\",\"cacheHit\":true},\"context\":{\"lastActivityMs\":\"-1\"}},{\"eventTimeMs\":1666392541139,\"latencyActionTicked\":{\"tickName\":\"pe\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"1297\"}},{\"eventTimeMs\":1666392541154,\"latencyActionTicked\":{\"tickName\":\"pot_isc\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"1312\"}},{\"eventTimeMs\":1666392541160,\"latencyActionTicked\":{\"tickName\":\"fs\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"1319\"}},{\"eventTimeMs\":1666392541169,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":51663,\"veCounter\":1}]},\"context\":{\"lastActivityMs\":\"1327\"}},{\"eventTimeMs\":1666392541170,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28240,\"veCounter\":2}]},\"context\":{\"lastActivityMs\":\"1328\"}},{\"eventTimeMs\":1666392541170,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28239,\"veCounter\":3}]},\"context\":{\"lastActivityMs\":\"1328\"}},{\"eventTimeMs\":1666392541170,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":28240,\"veCounter\":2},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1328\"}},{\"eventTimeMs\":1666392541170,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":28239,\"veCounter\":3},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1328\"}},{\"eventTimeMs\":1666392541171,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":36925,\"veCounter\":4}]},\"context\":{\"lastActivityMs\":\"1329\"}},{\"eventTimeMs\":1666392541171,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":23851,\"veCounter\":5}]},\"context\":{\"lastActivityMs\":\"1329\"}},{\"eventTimeMs\":1666392541173,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":108341,\"veCounter\":6}]},\"context\":{\"lastActivityMs\":\"1331\"}},{\"eventTimeMs\":1666392541174,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":139609,\"veCounter\":7}]},\"context\":{\"lastActivityMs\":\"1333\"}},{\"eventTimeMs\":1666392541175,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":140127,\"veCounter\":8}]},\"context\":{\"lastActivityMs\":\"1333\"}},{\"eventTimeMs\":1666392541175,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":151179,\"veCounter\":9}]},\"context\":{\"lastActivityMs\":\"1333\"}},{\"eventTimeMs\":1666392541175,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":145078,\"veCounter\":10}]},\"context\":{\"lastActivityMs\":\"1333\"}},{\"eventTimeMs\":1666392541176,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":139117,\"veCounter\":11}]},\"context\":{\"lastActivityMs\":\"1334\"}},{\"eventTimeMs\":1666392541176,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":139117,\"veCounter\":11},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1334\"}},{\"eventTimeMs\":1666392541179,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":6194,\"veCounter\":12}]},\"context\":{\"lastActivityMs\":\"1337\"}},{\"eventTimeMs\":1666392541179,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":36842,\"veCounter\":13}]},\"context\":{\"lastActivityMs\":\"1338\"}},{\"eventTimeMs\":1666392541180,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":36842,\"veCounter\":13},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1338\"}},{\"eventTimeMs\":1666392541180,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":6193,\"veCounter\":14}]},\"context\":{\"lastActivityMs\":\"1338\"}},{\"eventTimeMs\":1666392541180,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":6193,\"veCounter\":14},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1338\"}},{\"eventTimeMs\":1666392541181,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28662,\"veCounter\":15}]},\"context\":{\"lastActivityMs\":\"1339\"}},{\"eventTimeMs\":1666392541182,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":113681,\"veCounter\":16}]},\"context\":{\"lastActivityMs\":\"1340\"}},{\"eventTimeMs\":1666392541182,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":127299,\"veCounter\":17}]},\"context\":{\"lastActivityMs\":\"1340\"}},{\"eventTimeMs\":1666392541182,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28663,\"veCounter\":18}]},\"context\":{\"lastActivityMs\":\"1341\"}},{\"eventTimeMs\":1666392541183,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":62946,\"veCounter\":19}]},\"context\":{\"lastActivityMs\":\"1341\"}},{\"eventTimeMs\":1666392541183,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":139116,\"veCounter\":20}]},\"context\":{\"lastActivityMs\":\"1342\"}},{\"eventTimeMs\":1666392541184,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":139116,\"veCounter\":20},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1342\"}},{\"eventTimeMs\":1666392541184,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":139118,\"veCounter\":21}]},\"context\":{\"lastActivityMs\":\"1342\"}},{\"eventTimeMs\":1666392541185,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28656,\"veCounter\":22}]},\"context\":{\"lastActivityMs\":\"1343\"}},{\"eventTimeMs\":1666392541185,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":70344,\"veCounter\":23}]},\"context\":{\"lastActivityMs\":\"1344\"}},{\"eventTimeMs\":1666392541186,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":164503,\"veCounter\":24}]},\"context\":{\"lastActivityMs\":\"1344\"}},{\"eventTimeMs\":1666392541186,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28665,\"veCounter\":25}]},\"context\":{\"lastActivityMs\":\"1344\"}},{\"eventTimeMs\":1666392541186,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":28664,\"veCounter\":26}]},\"context\":{\"lastActivityMs\":\"1345\"}},{\"eventTimeMs\":1666392541187,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":86570,\"veCounter\":27}]},\"context\":{\"lastActivityMs\":\"1345\"}},{\"eventTimeMs\":1666392541188,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":16499,\"veCounter\":28}]},\"context\":{\"lastActivityMs\":\"1346\"}},{\"eventTimeMs\":1666392541190,\"visualElementAttached\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"parentVe\":{\"veType\":3854},\"childVes\":[{\"veType\":61214,\"veCounter\":29}]},\"context\":{\"lastActivityMs\":\"1348\"}},{\"eventTimeMs\":1666392541210,\"latencyActionTicked\":{\"tickName\":\"pot_ist\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"1368\"}},{\"eventTimeMs\":1666392541214,\"idbTransactionEnded\":{\"objectStoreNames\":\"databases\",\"connectionHasUnknownAbortedTransaction\":false,\"duration\":10,\"isSuccessful\":true,\"tryCount\":1,\"tag\":\"IDB_TRANSACTION_TAG_UNKNOWN\"},\"context\":{\"lastActivityMs\":\"1372\"}},{\"eventTimeMs\":1666392541226,\"idbTransactionEnded\":{\"objectStoreNames\":\"EntityStore,EntityAssociationStore\",\"connectionHasUnknownAbortedTransaction\":false,\"duration\":1,\"isSuccessful\":true,\"tryCount\":1,\"tag\":\"IDB_TRANSACTION_TAG_UNKNOWN\"},\"context\":{\"lastActivityMs\":\"1384\"}},{\"eventTimeMs\":1666392541233,\"idbTransactionEnded\":{\"objectStoreNames\":\"EntityStore,EntityAssociationStore\",\"connectionHasUnknownAbortedTransaction\":false,\"duration\":6,\"isSuccessful\":true,\"tryCount\":1,\"tag\":\"IDB_TRANSACTION_TAG_UNKNOWN\"},\"context\":{\"lastActivityMs\":\"4\"}},{\"eventTimeMs\":1666392541233,\"offlineStateSnapshot\":{\"offlineVideos\":[]},\"context\":{\"lastActivityMs\":\"5\"}},{\"eventTimeMs\":1666392541367,\"latencyActionTicked\":{\"tickName\":\"pot_if\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"24\"}},{\"eventTimeMs\":1666392541368,\"latencyActionTicked\":{\"tickName\":\"pot_cms\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"24\"}},{\"eventTimeMs\":1666392541368,\"latencyActionTicked\":{\"tickName\":\"pot_cmf\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"24\"}},{\"eventTimeMs\":1666392541625,\"visualElementHidden\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CMEBEIf2BBgHIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":8},\"context\":{\"lastActivityMs\":\"281\"}},{\"eventTimeMs\":1666392541625,\"visualElementHidden\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CLcBEIf2BBgIIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":8},\"context\":{\"lastActivityMs\":\"281\"}},{\"eventTimeMs\":1666392542302,\"latencyActionTicked\":{\"tickName\":\"cmi\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"11\"}},{\"eventTimeMs\":1666392546108,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CPQBENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1082\"}},{\"eventTimeMs\":1666392546109,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CJsBENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1083\"}},{\"eventTimeMs\":1666392546158,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CJUBENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1132\"}},{\"eventTimeMs\":1666392546158,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CI8BENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1132\"}},{\"eventTimeMs\":1666392546173,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CIkBENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1147\"}},{\"eventTimeMs\":1666392546173,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CIMBENwwIhMIprGz-rPy-gIVI8ZPCB3ynAn4\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1147\"}},{\"eventTimeMs\":1666392546173,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CH0Q3DAiEwimsbP6s_L6AhUjxk8IHfKcCfg=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1147\"}},{\"eventTimeMs\":1666392546192,\"visualElementShown\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"trackingParams\":\"CHcQ3DAiEwimsbP6s_L6AhUjxk8IHfKcCfg=\"},\"eventType\":1},\"context\":{\"lastActivityMs\":\"1166\"}}],\"serializedClientEventId\":{\"serializedEventId\":\"2iFTY8rwDpHX7QSQj7mwDg\",\"clientCounter\":\"10637\"}}",
  "method": "POST"
}); ;
fetch("https://www.youtube.com/youtubei/v1/log_event?alt=json&key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "SAPISIDHASH 1666392556_04f06b87f5c27ab866f6360ed85aac61c9987dc0",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "x-goog-authuser": "",
    "x-goog-pageid": "undefined",
    "x-goog-request-time": "1666392556769",
    "x-goog-visitor-id": "CgtGM3NPWHp6UWZyQSjaw8yaBg%3D%3D",
    "x-origin": "https://www.youtube.com",
    "x-youtube-ad-signals": "dt=1666392539831&flash=0&frm&u_tz=180&u_his=2&u_h=1080&u_w=1920&u_ah=1040&u_aw=1920&u_cd=24&bc=31&bih=969&biw=1485&brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1040%2C1501%2C969&vis=1&wgl=true&ca_type=image&bid=ANyPxKoBiRuo2Hakl2JDFnChLNfh9AS1BIQT4_64_tvlLo3K84G61EOKDUU-pWFC-2kIa6OrsquiuOarNgeZfDtlmZPvEPzZQQ",
    "x-youtube-client-name": "1",
    "x-youtube-client-version": "2.20221021.00.00",
    "x-youtube-device": "cbr=Chrome&cbrver=106.0.0.0&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0&cplatform=DESKTOP",
    "x-youtube-page-cl": "482690998",
    "x-youtube-page-label": "youtube.desktop.web_20221021_00_RC00",
    "x-youtube-time-zone": "Etc/GMT-3",
    "x-youtube-utc-offset": "180",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"context\":{\"client\":{\"hl\":\"ru\",\"gl\":\"RU\",\"clientName\":1,\"clientVersion\":\"2.20221021.00.00\",\"configInfo\":{\"appInstallData\":\"CNrDzJoGEKjUrgUQuIuuBRDiua4FELKI_hIQ28quBRCZxq4FEOrKrgUQm8quBRDpjf4SEOrVrgUQ1IOuBRCJj_4SENi-rQUQkfj8Eg%3D%3D\"},\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36\",\"mainAppWebInfo\":{\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\"},\"memoryTotalKbytes\":\"8000000\",\"connectionType\":\"CONN_CELLULAR_4G\",\"browserName\":\"Chrome\",\"browserVersion\":\"106.0.0.0\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"platform\":\"DESKTOP\"}},\"events\":[{\"eventTimeMs\":1666392556764,\"sliEventBatch\":{\"loggedEvents\":[{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false},\"survivalSli\":{\"partitionMinute\":10,\"survivalStatus\":\"SURVIVAL_STATUS_TYPE_ALIVE_START\"},\"csn\":\"UNDEFINED_CSN\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_SESSION_PARTITION\",\"state\":\"SLI_STATE_END\",\"status\":\"SLI_STATUS_SUCCESS\"}]},{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false,\"pageType\":\"MAIN_APP_WEB_PAGE_TYPE_BROWSE\"},\"csn\":\"UNDEFINED_CSN\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_APP_BOOTS\",\"state\":\"SLI_STATE_START\",\"sliId\":\"spmkAHOz\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_YT_INITIAL_DATA_PRESENT\",\"state\":\"SLI_STATE_START\",\"sliId\":\"o5YLM1tq\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_APP_BOOTS\",\"status\":\"SLI_STATUS_SUCCESS\",\"state\":\"SLI_STATE_END\",\"sliId\":\"spmkAHOz\"}]},{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false},\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_STFE_GREATER_THAN_ONE_MINUTE\",\"state\":\"SLI_STATE_START\",\"sliId\":\"9XUJ6XQ4\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_STFE_GREATER_THAN_TEN_MINUTES\",\"state\":\"SLI_STATE_START\",\"sliId\":\"8HdKqSpH\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_SERVICE_WORKER_REGISTRATION\",\"state\":\"SLI_STATE_START\",\"sliId\":\"rcIa2bI7\"}]},{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false,\"pageType\":\"MAIN_APP_WEB_PAGE_TYPE_BROWSE\"},\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_YT_INITIAL_DATA_PRESENT\",\"status\":\"SLI_STATUS_SUCCESS\",\"state\":\"SLI_STATE_END\",\"sliId\":\"o5YLM1tq\"}]},{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false},\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_YT_GUIDE_DATA_PRESENT\",\"state\":\"SLI_STATE_START\",\"sliId\":\"deqO1CF4\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_NETWORK_REQUEST\",\"state\":\"SLI_STATE_START\",\"sliId\":\"cvhykQO0\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_SERVICE_WORKER_REGISTRATION\",\"status\":\"SLI_STATUS_SUCCESS\",\"state\":\"SLI_STATE_END\",\"sliId\":\"rcIa2bI7\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_NETWORK_REQUEST\",\"status\":\"SLI_STATUS_SUCCESS\",\"state\":\"SLI_STATE_END\",\"sliId\":\"cvhykQO0\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_YT_GUIDE_DATA_PRESENT\",\"status\":\"SLI_STATUS_SUCCESS\",\"state\":\"SLI_STATE_END\",\"sliId\":\"deqO1CF4\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_STFE_GREATER_THAN_ONE_MINUTE\",\"status\":\"SLI_STATUS_ABORTED\",\"state\":\"SLI_STATE_END\",\"sliId\":\"9XUJ6XQ4\"},{\"name\":\"SLI_NAME_YOUTUBE_WEB_STFE_GREATER_THAN_TEN_MINUTES\",\"status\":\"SLI_STATUS_ABORTED\",\"state\":\"SLI_STATE_END\",\"sliId\":\"8HdKqSpH\"}]}],\"unloggedEvents\":[]},\"context\":{\"lastActivityMs\":\"868\"}},{\"eventTimeMs\":1666392556764,\"latencyActionTicked\":{\"tickName\":\"aa\",\"clientActionNonce\":\"K9KHt66xuhpAq_Le\"},\"context\":{\"lastActivityMs\":\"868\"}},{\"eventTimeMs\":1666392556764,\"foregroundHeartbeat\":{\"firstActivityMs\":\"15536\",\"clientDocumentNonce\":\"t9RlU0CbXYr7ulPw\",\"index\":\"1\",\"lastEventDeltaMs\":\"16922\",\"trigger\":\"FOREGROUND_HEARTBEAT_TRIGGER_ON_BACKGROUND\"},\"context\":{\"lastActivityMs\":\"869\"}},{\"eventTimeMs\":1666392556765,\"visualElementHidden\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\",\"ve\":{\"veType\":3854},\"eventType\":16},\"context\":{\"lastActivityMs\":\"869\"}},{\"eventTimeMs\":1666392556765,\"sliEventBatch\":{\"loggedEvents\":[{\"dimensions\":{\"mainAppWeb\":{\"isShellLoad\":false},\"survivalSli\":{\"partitionMinute\":10,\"survivalStatus\":\"SURVIVAL_STATUS_TYPE_CENSORED\"},\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\"},\"records\":[{\"name\":\"SLI_NAME_YOUTUBE_WEB_SESSION_PARTITION\",\"state\":\"SLI_STATE_END\",\"status\":\"SLI_STATUS_SUCCESS\"}]}],\"unloggedEvents\":[]},\"context\":{\"lastActivityMs\":\"869\"}},{\"eventTimeMs\":1666392556766,\"finalPayload\":{\"csn\":\"MC41OTc2MjA5NDA3NDY1NzQ1\"},\"context\":{\"lastActivityMs\":\"871\"}}],\"serializedClientEventId\":{\"serializedEventId\":\"2iFTY8rwDpHX7QSQj7mwDg\",\"clientCounter\":\"10638\"}}",
  "method": "POST"
}); ;
fetch("https://i.ytimg.com/generate_204", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/desktop_polymer.vflset/desktop_polymer.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/web-animations-next-lite.min.vflset/web-animations-next-lite.min.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/custom-elements-es5-adapter.vflset/custom-elements-es5-adapter.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/webcomponents-sd.vflset/webcomponents-sd.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/intersection-observer.min.vflset/intersection-observer.min.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/scheduler.vflset/scheduler.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-i18n-constants-ru_RU.vflset/www-i18n-constants.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/www-tampering.vflset/www-tampering.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/spf.vflset/spf.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/jsbin/network.vflset/network.js", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=YouTube+Sans:wght@300..900&display=swap", {
  "headers": {
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-main-desktop-home-page-skeleton.css", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-onepick.css", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.UrU5vkUWQCM.L.B1.O/am=AAE/d=0/br=1/rs=AGKMywEbyb0j4PcxSqqEUJ0-d7GCQna4fg", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu4mxK.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://fonts.googleapis.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.gstatic.com/youtube/img/emojis/emojis-svg-9.json", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://googleads.g.doubleclick.net/pagead/id", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "IDE=AHWqTUnG90D8vKZ6M_hjdqjmCq8U3s3VtxMuaUg9DJ37-JJV5PFHnIac2NAssXldxaQ",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu5mxKOzY.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://fonts.googleapis.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/search/audio/failure.mp3", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "range": "bytes=0-",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "audio",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/search/audio/no_input.mp3", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "range": "bytes=0-",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "audio",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/search/audio/open.mp3", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "range": "bytes=0-",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "audio",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/search/audio/success.mp3", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "range": "bytes=0-",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "audio",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/s/desktop/41dc17d1/cssbin/www-main-desktop-watch-page-skeleton.css", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmEU9fBBc4.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://fonts.googleapis.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmEU9fABc4EsA.woff2", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://fonts.googleapis.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.youtube.com/youtubei/v1/guide?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "SAPISIDHASH 1666392558_1de20d69fe4e1fef1c3fec9efa149043b3bccfb1",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "x-goog-authuser": "0",
    "x-goog-visitor-id": "CgtGM3NPWHp6UWZyQSjrw8yaBg%3D%3D",
    "x-origin": "https://www.youtube.com",
    "x-youtube-bootstrap-logged-in": "false",
    "x-youtube-client-name": "1",
    "x-youtube-client-version": "2.20221021.00.00",
    "cookie": "VISITOR_INFO1_LIVE=F3sOXzzQfrA; CONSENT=WP.28e13f.28e24e.28e33e; PREF=tz=Etc.GMT-3&f5=20000; __Secure-3PSID=MAhsvejNBiN9v1PJxEaQ2TIz8it-LcuiC38crxIQXVRDL3v1nt1310_w-HwgqHTmMiDrpQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AEf-XMRlQPpQGgH4IC7ucPylzpPknKnaBqasRFbxQXGg9hXBbdNYwnwpyNjGKvhm25FrTiP2Edo; YSC=UWm9_Y64kz4; GPS=1",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"context\":{\"client\":{\"hl\":\"ru\",\"gl\":\"RU\",\"remoteHost\":\"95.161.248.163\",\"deviceMake\":\"\",\"deviceModel\":\"\",\"visitorData\":\"CgtGM3NPWHp6UWZyQSjrw8yaBg%3D%3D\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36,gzip(gfe)\",\"clientName\":\"WEB\",\"clientVersion\":\"2.20221021.00.00\",\"osName\":\"Windows\",\"osVersion\":\"10.0\",\"originalUrl\":\"https://www.youtube.com/\",\"platform\":\"DESKTOP\",\"clientFormFactor\":\"UNKNOWN_FORM_FACTOR\",\"configInfo\":{\"appInstallData\":\"COvDzJoGEOrKrgUQ28quBRCZxq4FEOmN_hIQ4rmuBRDq1a4FELKI_hIQuIuuBRCo1K4FENSDrgUQm8quBRCJj_4SEJH4_BIQ2L6tBQ%3D%3D\"},\"timeZone\":\"Etc/GMT-3\",\"browserName\":\"Chrome\",\"browserVersion\":\"106.0.0.0\",\"acceptHeader\":\"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\",\"deviceExperimentId\":\"CgtPX3FBSUg1cE5XbxDrw8yaBg%3D%3D\",\"screenWidthPoints\":1501,\"screenHeightPoints\":969,\"screenPixelDensity\":1,\"screenDensityFloat\":1,\"utcOffsetMinutes\":180,\"userInterfaceTheme\":\"USER_INTERFACE_THEME_LIGHT\",\"memoryTotalKbytes\":\"8000000\",\"mainAppWebInfo\":{\"graftUrl\":\"https://www.youtube.com/\",\"pwaInstallabilityStatus\":\"PWA_INSTALLABILITY_STATUS_UNKNOWN\",\"webDisplayMode\":\"WEB_DISPLAY_MODE_BROWSER\",\"isWebNativeShareAvailable\":true}},\"user\":{\"lockedSafetyMode\":false},\"request\":{\"useSsl\":true,\"internalExperimentFlags\":[],\"consistencyTokenJars\":[]},\"adSignalsInfo\":{\"params\":[{\"key\":\"dt\",\"value\":\"1666392557373\"},{\"key\":\"flash\",\"value\":\"0\"},{\"key\":\"frm\",\"value\":\"0\"},{\"key\":\"u_tz\",\"value\":\"180\"},{\"key\":\"u_his\",\"value\":\"2\"},{\"key\":\"u_h\",\"value\":\"1080\"},{\"key\":\"u_w\",\"value\":\"1920\"},{\"key\":\"u_ah\",\"value\":\"1040\"},{\"key\":\"u_aw\",\"value\":\"1920\"},{\"key\":\"u_cd\",\"value\":\"24\"},{\"key\":\"bc\",\"value\":\"31\"},{\"key\":\"bih\",\"value\":\"969\"},{\"key\":\"biw\",\"value\":\"1485\"},{\"key\":\"brdim\",\"value\":\"0,0,0,0,1920,0,1920,1040,1501,969\"},{\"key\":\"vis\",\"value\":\"1\"},{\"key\":\"wgl\",\"value\":\"true\"},{\"key\":\"ca_type\",\"value\":\"image\"}],\"bid\":\"ANyPxKr7b0SekOcRilQ2M4WVXAqQ3cN54DwywUtdZvMhueHy9wkVdNQNqwbdFdwb-SomCSL6qwbC4K9VIpNqlrFMvhmqV5gksQ\"}},\"fetchLiveState\":true}",
  "method": "POST"
}); ;
fetch("https://www.google.com/pagead/lvz?evtid=ABLloLk5o0ELmOmQrFge_U9LBnc-AyhiTnZ5j9NlFkW8c4p6cUNHURix5M3kKCApNZdyhQBQiT1zOC_pEPAANyqf7aqOI8FoFA&req_ts=1666392556&pg=MainAppBootstrap%3AHome&az=1&sigh=AFmDhKdyIwPbWdB_VpEhZX7g44MxaUtpmw", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "__Secure-3PSID=PQhsvVgSw8fYdB5KIFfg0MDnbroBQHw47B1z-7-x7bXSVR-0ml2vpKyCaavZM7-RfomeRQ.; __Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSIDCC=AIKkIs1DH_5lJpd2OkwX4NgP392elABKwOBTuCJwI6yhw95EhnVWbGmGX5CbVDOf2jfnKYcPkg; 1P_JAR=2022-10-21-22; NID=511=sM8cbyLlUMimZFIVpjUEF6GTHqR86uNiyY3tbgtQsDzn1dzMzW1C6DI2-Sfc5mq5LD93_99QJKjI0mPMBW0XVHf6-j1NH75J4EFNxf_eTIeSb424_1yS79houMGlEpW-3OzaFZHjZ9iVqhcnHLQAV80pRtt94JfXx1Uiw2lxj2osPcGC6zLXwkpLx9PaTEFLLYAOe2bZaNtHNMIphmMJuSKfL1hRTOhUKv5Ky6eX1WRZeJTs50WD6fn6HniVgQld_uQa_xuoDPOiEUen0PMjO5WWzZXryflMHJQpQML8QRS0yV6pDF3O9TO_bY4BNB39jmHlQe56iIPWjDMQLZexISe27J_WpSOgfEZ4YEO7Bcv_LMJosTqsTBgQxs5iGabAvdvKNe3AXUZokIeRuh4pqlvLkWmWbM9MZ7J8eNL1npo",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://www.google.ru/pagead/lvz?evtid=ABLloLk5o0ELmOmQrFge_U9LBnc-AyhiTnZ5j9NlFkW8c4p6cUNHURix5M3kKCApNZdyhQBQiT1zOC_pEPAANyqf7aqOI8FoFA&req_ts=1666392556&pg=MainAppBootstrap%3AHome&az=1&sigh=AFmDhKdyIwPbWdB_VpEhZX7g44MxaUtpmw", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "cookie": "__Secure-3PAPISID=7OM5PMRZ0yfUKINS/A0OHty6Zf2g2Ueh8p; __Secure-3PSID=PwhsveYhxB--ikj6yrID0rLaCbx4dYKq_tkx_SCr7nxqlrpMDpVxcuZbdIYIi_e8lZTFnQ.; 1P_JAR=2022-10-21-22; NID=511=djAha0l0V5NGRxU1_T7Kg-4-gmL-Gan5n7sihqgVC8ydV5RBYVXmFTuC6Oa0uI2Bpr-dJp55snWDlzuQqlKa7FmilUEXvKtxZZo3MHOeNsrdz8HjCNR1OpTzriqw7p8fydDEX09DqWMAM5bHYcFPYYkvjXfQuy6JHO-dySZuSvTVzTZPmzfoN4fa5a7ciUl2GCFdmlqTviqpiZvA755K1PjBFs18153caKHGuc_19V5tzcWFIZf2SWjKVL-r7D3HqlzriQMaj9_vYFPkhgwyKw-dWPly8APpDfs623IaEyEA1ZZUflYUBr6cKLgSbQrEKZ_T3BVApv5tSKbjtprIKxlwVTfPyQRU1-XHRha_-Q",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://i.ytimg.com/vi/p09i_hoFdd0/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBxhquYa_rwu1OzAyTbLCC5Vu5WFw", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://yt3.ggpht.com/ytc/AMLnZu8hv8SPL-36xQYUGUysRvP8W0cTmtRglPeuVARliA=s68-c-k-c0x00ffffff-no-rj", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://i.ytimg.com/vi/dgA5zDpwZ4s/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDkmqYpx-jMEKvPQV937k46DfgStA", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://yt3.ggpht.com/ytc/AMLnZu_TQzppFEKhitrAyP_L1RrcM9KJl9DI9oKzPWquWA=s68-c-k-c0x00ffffff-no-rj", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://i.ytimg.com/vi/LKgAAx3Z7BA/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAtiCez1TcG2vkXP9XIHsTLTHaXkg", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://yt3.ggpht.com/ytc/AMLnZu9cVr3u07WNOIXv1E3qwpYIeJVD1pkr4MmyryB92g=s68-c-k-c0x00ffffff-no-rj", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://i.ytimg.com/vi/jfKfPfyJRdk/hq720_live.jpg?sqp=COzBzJoG-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB7Hy7huR-fu3Mj5qDujhleyD4hRQ", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://yt3.ggpht.com/KNYElmLFGAOSZoBmxYGKKXhGHrT2e7Hmz3WsBerbam5uaDXFADAmT7htj3OcC-uK1O88lC9fQg=s68-c-k-c0x00ffffff-no-rj", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
}); ;
fetch("https://i.ytimg.com/vi/NG0AkNg-d8g/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCh03SOVhwe0Je9qLm5UTUv__t-8w", {
  "headers": {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"106.0.5249.119\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"106.0.5249.119\", \"Google Chrome\";v=\"106.0.5249.119\", \"Not;A=Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "x-client-data": "CIe2yQEIo7bJAQjBtskBCKmdygEI+OHKAQiUocsBCOG7zAEI8rzMAQjAxswBCOLLzAEIn9HMAQjj2MwBCL7dzAEIxOHMAQjG4cwBCPrmzAEI2OjMAQj/6MwBCJvqzAEI4evMAQ==",
    "Referer": "https://www.youtube.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
