# [Web]Baby's SQLi - Stage 1- 100pts
困ったな……どうしよう……．\
ぱろっく先生がキャッシュカードをなくしてしまったショックからデータベースに逃げ込んでしまったんだ．\
うーん，君SQL書くのうまそうだね．ちょっと僕もWeb問作らなきゃいけないから，連れ戻すのを任せてもいいかな？\
多分，ぱろっく先生はそこまで深いところまで逃げ込んで居ないと思うんだけども……．\

とりあえず，逃げ込んだ先は以下のURLだよ．\
一応，報酬としてフラグを用意してるからよろしくね！

https://ctf.spica.bz/baby_sql/

Caution
- sandbox.spica.bzの80,443番ポート以外への攻撃は絶対にしないようにお願いします．
- あなたが利用しているネットワークへの配慮のためhttpsでの通信を推奨します．

# Solution
SQL文がそのまま動作するようなので、`select * from palloc_home;` を送信することでフラグが表示された。