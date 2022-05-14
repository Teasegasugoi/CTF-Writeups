# 参考サイト
# https://note.nkmk.me/python-requests-usage/
import requests
import time

url = 'https://crumbs.web.actf.co/'

response = requests.get(url)
curr = response.text.replace('Go to ', '')

for i in range(1000):
    res = requests.get(url + curr)
    curr = res.text.replace('Go to ', '')
    print('{index}: {path}'.format(index=i, path=curr))
    time.sleep(2)