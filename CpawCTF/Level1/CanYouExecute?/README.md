# [Reversing] Can you execute ? 10pts
拡張子がないファイルを貰ってこのファイルを実行しろと言われたが、どうしたら実行出来るのだろうか。
この場合、UnixやLinuxのとあるコマンドを使ってファイルの種類を調べて、適切なOSで実行するのが一般的らしいが…\
問題ファイル： exec_me
# Solution
拡張子がないファイルなのでとりあえずfileコマンドを用いてファイル形式を調べた。

```bash
$ file exec_me
> exec_me: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=663a3e0e5a079fddd0de92474688cd6812d3b550, not stripped
```

ELFファイルとは、Linux 上で実行可能なプログラムやそれにリンクされる共有ライブラリなどのバイナリファイルのファイル形式のこと。

ファイルのパーミッションの確認を行った。

```bash
$ ls -l exec_me
> -rw-r--r--@ 1 xxxx  staff  8556  3 17 04:21 exec_me
```

`-rw-r—r—` が示す10文字は、<ファイルの種>/<ファイルの所有者(3文字)>/<ファイルの所有グループ(3文字)>/<その他(3文字)> それぞれの権限を示している。r は読み取り、w は書き取り、x は実行 を示している。従って、exec_me は実行権限がないことがわかる。よって、実行権限を付与した。

```bash
$ chmod 764 exec_me
$ ls -l exec_me
> -rwxrw-r--@ 1 xxxx  staff  8556  3 17 04:21 exec_me
$ ./exec_me
cpaw{Do_you_know_ELF_file?}
```

権限が変わっているのがわかる。