# [MISC] Confetti 40pts
"From the sky, drop like confetti All eyes on me, so V.I.P All of my dreams, from the sky, drop like confetti" - Little Mix

# Solution
初見で解けなかった。\
pngファイルの中にフラグが隠されているであろう問題。identifyで情報をみてみる。ここで詰んだ。\
[writeup](https://ctftime.org/writeup/33775)をよむ。\
binwalkとよばれる、ファイルの種別を調べたり、ファイルの中にファイルが含まれているファイルからファイルを抽出できるコマンドがキーだったらしい。\
binwalkコマンドの簡単な使い方 
```shell
# ファイルに何が含まれているか表示
$ binwalk {ファイル名}

# ファイルを抽出
$ binwalk --dd="{抜き出したい拡張子など}" {ファイル名}
```
抽出したフォルダの中にフラグが書かれたpngファイルが存在。