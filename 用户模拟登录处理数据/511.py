# 获取cookie，带着cookie请求url
# 使用session请求
import requests

session = requests.Session()

url = 'https://passport.17k.com/'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
data = {
    'loginName': '18955336286',
    'password': '199712090054lzg'
}

response = session.post(url=url,data=data,headers=headers)
response.encoding = 'utf-8'

print(response.text)


