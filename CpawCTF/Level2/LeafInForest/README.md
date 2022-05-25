# [Forensic] leaf in forest 100pts
このファイルの中にはフラグがあります。探してください。\
フラグはすべて小文字です！
# Solution
ファイルの中身を見ると、`lovelive!` が繰り返されている。ただ、たまにそれ以外の文字が含まれていることが分かるので、この文字列だけを削除することでフラグが得られそう。
Pythonを使って、文字列変換作業に取り掛かる。
```python
import re
with open('misc100.txt', 'r', encoding="utf8", errors='ignore') as f:
        read_data = f.read()
        data = read_data.replace('live!', '')
        data = data.replace('love', '')
        data = data.replace('!','')
        data = re.sub(r'[a-z]*','', data)
        print(data)
```
絶対もっといい解決策ある