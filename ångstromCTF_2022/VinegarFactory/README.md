# [CRYPTO] Vinegar Factory 100pts
Clam managed to get parole for his dumb cryptography jokes, but after making yet another dumb joke on his way out of the courtroom, he was sent straight back in. This time, he was sentenced to 5 years of making dumb Vigenere challenges. Clam, fed up with the monotony of challenge writing, made a program to do it for him. Can you solve enough challenges to get the flag?

Connect to the challenge at `nc challs.actf.co 31333`.\
Hint\
You'll have to script the solution since the server has a 20 second timeout. pwntools is very helpful for scripting IO.
# Solution
解法をざっくり説明すると、サーバーにアクセスして得られる暗号文を復号して送り返す という作業を50回繰り返す。\
ヒントより手作業で行うと時間が足りないため、何かしら自動化する必要がある。solution.py に復号化に用いた関数を記している。問題のサーバーが対話形式を採用していたため、どうやって50回復号化するかめちゃくちゃ悩んだ。ターミナルとの対話を可能にするexpectというものがあるらしく、それを用いたらいけそうだった。expectの書き方がよくわからなくて時間がかかりそうだったが、python版expectのPexpectというものがあり、それを用いたらフラグを入手できた。\
CRYPTOのwriteup書くの難しいから、解くのに使ったコード載せることしかできない（ ;  ; ）