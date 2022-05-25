# [Reversing]reversing easy! 100pts
フラグを出す実行ファイルがあるのだが、プログラム(elfファイル)作成者が出力する関数を書き忘れてしまったらしい…
# Solution
```bash
$ strings rev100
>
~~~
D$Fcpawf
D$J{
D$ y
D$$a
D$(k
D$,i
D$0n
D$4i
D$8k
D$<u
D$@!
~~~
```
フラグっぽい文字列発見だけど、作者が意図した解き方ではなさそう。