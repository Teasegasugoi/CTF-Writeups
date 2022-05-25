# [Crypto]Block Cipher 100pts
与えられたC言語のソースコードを読み解いて復号してフラグを手にれましょう。

暗号文：cpaw{ruoYced_ehpigniriks_i_llrg_stae}
# Solution
コマンドライン引数を持つプログラムなので、`./{fileName} {暗号文} {key}` で出てきそう。

```bash
# コンパイル
$ gcc crypto100.c -o crypto100

＄./crypto100 {暗号文} 4
```