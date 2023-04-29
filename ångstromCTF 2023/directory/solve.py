# https://youtu.be/fe5O1wUSkIE?t=222 によると, wget で一括DLしてから行った方がいい?

import requests

url = "https://directory.web.actf.co"

def get_url(url):
  r = requests.get(url)
  return r.text

def solve():
  for i in range(4999, -1, -1):
    print(i)
    page = "/" + str(i) + ".html"
    result = get_url(url + page)
    if result != "your flag is in another file":
      print(f"{page}: {result}")
      break

solve()