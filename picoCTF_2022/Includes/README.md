# [Web] Includes 100pts
Can you get the flag?
Go to this [website](http://saturn.picoctf.net:57833/) and see what you can discover.

# Solution
includeについての説明が書かれているサイト。ページ下には `Say hello` と書かれたボタンがあり、押すとアラートで `This code is in a separate file!`と表示される。ファイル分割がテーマっぽいので、検証ツールでNetworkを参照すると、`saturn.picoctf.net`, `style.css`, `script.js` の3ファイルが存在。後ろ2つのファイルにフラグが分割して書かれていた。