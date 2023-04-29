import requests

url = 'https://pioneer.tailec718.ts.net/'
headers = {'host': 'flag.local'}

response = requests.get(url, headers=headers)

print(response.text)