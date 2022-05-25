# [Misc]Image! 100pts
Find the flag in this zip file.
# Solution
misc100.zip というファイルからflagを探す問題

```bash
$ file misc100.zip
> misc100.zip: OpenDocument Drawing
```

OpenDocument は XMLをベースとしたオフィススイート用のファイルフォーマットらしい。拡張子を .odt に変更して word で開いて終了。