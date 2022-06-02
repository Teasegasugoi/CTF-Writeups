# Cookies 40pts
AUTHOR: MADSTACKS

Description
Who doesn't love cookies? Try to figure out the best one.\
http://mercury.picoctf.net:6418/
# Solution
入力フォームが1つあるサイトでの問題。\
とりあえず `1234` で送信してみると、`That doesn't appear to be a valid cookie.` と表示される。どうやら、正しいクッキーを入力しないといけないみたいである。検証ツールでCookieの値を確認してみると、`name=-1` となっていた。\
プレースホルダに `snickerdoodle` と書かれていたので、この文字列を試しに送信してみると `That is a cookie! Not very special though...` と最初とは異なる結果が表示された。この時のCookieの値は `name=0` になっていた。このことから、このサイトはCookieの値で結果を表示していると推測できる。\
BurpSuite でCookieの値を1ずつ増やしてリクエストを送ると、`name=18` の時に正解のフラグが書かれていた。