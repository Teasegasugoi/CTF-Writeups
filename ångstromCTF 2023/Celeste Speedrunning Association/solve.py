import time
import requests

url="https://mount-tunnel.web.actf.co"

def get_timestamp():
    return int(round(time.time() * 1000))

def solve():
  now = get_timestamp()
  data = {
    "start": now+1,
  }
  r = requests.post(url + "/submit", data)
  print(r.text)

solve()