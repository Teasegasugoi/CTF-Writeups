# [WEB] The Flash 40pts
The new Justice League movies nerfed the Flash, so clam made [his own rendition](https://the-flash.web.actf.co/)! Can you get the flag before the Flash swaps it out at the speed of light?\
Hint\
If only browsers had a way to inspect DOM changes...
# Solution
DOMの変化を読み取る問題。デベロッパーツールでDOMの変化を監視することができる。
1. デベロッパーツールを表示
2. 任意の場所で右クリック
3. break on を選択
4. subtree modification を選択
5. DOMが変化すると、画面を自動で止めてくれるので、1動作ずつ表示させていくと、フラグを見ることができる