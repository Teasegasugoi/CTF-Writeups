# GET aHEAD 20pts
AUTHOR: MADSTACKS

Description
Find the flag being held on this server to get ahead of the competition\
http://mercury.picoctf.net:53554/

Hint1: Maybe you have more than 2 choices\
Hint2: Check out tools like Burpsuite to modify your requests and look at the responses

# Solution
指定されたリンクに飛ぶと、`Choose Red` と `Choose Blue` と書かれたボタンが表示されているサイトが現れた。`Choose Red` を押すと背景が赤色、`Choose Blue` を押すと背景が青色に変化するみたいだ。検証ツールでコードを確認すると、この切り替えはJSではなく、`GET` と `POST` で行っていることが判明する。この問題のタイトルから `HEAD` メソッドでリクエストをすると、フラグが出現した。
HEADメソッドの存在を初めて知ったので、調べてみた。
> HEADメソッドとは、HTTP通信でクライアント（Webブラウザなど）からWebサーバへ送るリクエストの種類の一つで、当該資源のヘッダのみを送るよう要求するもの。データ本体（ボディ部）は受け取りたくない旨を伝える。

ほげえ...

# Reference
- https://e-words.jp/w/HEAD%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89.html