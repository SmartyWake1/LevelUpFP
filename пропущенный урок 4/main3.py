import requests
r = requests.get('https://vk.com/feed', auth=('user', 'pass'))
print(r.text)