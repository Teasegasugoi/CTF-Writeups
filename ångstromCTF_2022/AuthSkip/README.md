# [WEB] Auth Skip 40pts
Clam was doing his angstromCTF flag% speedrun when he ran into [the infamous timesink](https://auth-skip.web.actf.co/) known in the speedrunning community as "auth". Can you pull off the legendary auth skip and get the flag?\
[Source](https://files.actf.co/6abd10658e6dadacc1a15ae557f858ddf1b5f32b97788ed4727938afee2fd2bb/index.js)\
Hint\
Do you need the server to log in?
# Solution
初見で解けた。\
ソースファイルを読むと、passwordが `Math.random().toString()`となっているので、特定することが不可能であることがわかる。ちなみにこれは0以上1より小さい値をランダムに返す。

求めたいフラグはパスが `/` のときに `cookies.user` が admin で得られるらしい。

検証ツール → Application → Cookies で Name を user, Value を admin に設定したら、フラグが出現した。