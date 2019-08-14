import requests
url='http://www.bluecore.com.cn/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
response=requests.get(url,headers)
html=response.content.decode('utf-8')
with open('bluecore.html','w',encoding='utf-8')as f:
    f.write(html)