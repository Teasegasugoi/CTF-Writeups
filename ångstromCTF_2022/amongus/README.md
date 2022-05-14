# [MISC] amongus 40pts

One of these is not like the others.

# Solution
初見で解けた。\
.tar.gzip の中に似たようなテキストファイルがたくさん含まれていて、その中から異なるものを見つける問題。pythonでディレクトリ内のファイルをループするようなコードを書いた。

```shell
$ grep -rl -v {検索したい文字列}
```
でもいける。 `-rl` でサブディレクトリ内のファイルも含めて検索可能