# [Web] Roboto Sans 200pts
The flag is somewhere on this web application not necessarily on the website. Find it.
Check [this](http://saturn.picoctf.net:64710/) out.
# Solution
問題文より脳死で `/robots.txt` でアクセス。案の定ヒットする。真ん中の意味不明な文字列をbase64でデコードすると、`js/myfile.txt` となり、これにアクセスすると、フラグがわかる。
`robots.txt` に脳死でアクセスできて成長を感じたw