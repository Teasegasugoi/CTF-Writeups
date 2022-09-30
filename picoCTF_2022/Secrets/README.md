# [Web] Secrets 200pts
We have several pages hidden. Can you find the one with the flag?
The website is running [here](http://saturn.picoctf.net:49917/).

# Solution
ソースコードを確認すると、CSSファイルは `secret/assets/` に置いてあることがわかる。そこで、`secret/` を参照してみると以下のようなページが表示された。
![secrets1](images/secrets1.png)
このページのCSSファイルパスを確認すると、`hidden/file.css` であるので、`secret/hidden/` を調べてみると以下のページが表示された。
![secrets2](images/secrets2.png)
このページで使われているCSSファイルパスは `superhidden/login.css` であるので、`/secret/hidden/superhidden/` を調べてみると以下のページが表示された。
![secrets3](images/secrets3.png)
このページのソースコードを確認すると、フラグが置かれていた。