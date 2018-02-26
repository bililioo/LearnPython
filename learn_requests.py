# -*- coding: utf-8 -*-

import requests
# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)

# req = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(req.url)
# print(req.content)

# req1 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(req1.json())
# print(req1.encoding)

# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
# req2 = requests.get('https://www.douban.com/', headers=headers)
# print(req2.text)

data = {'form_email': 'abc@example.com', 'form_password': '123456'}
req3 = requests.post('https://accounts.douban.com/login', data=data)
print(req3.content