# Scavenger Hunt 50pts
AUTHOR: MADSTACKS

Description\
There is some interesting information hidden around this site http://mercury.picoctf.net:27278/. Can you find it?\
Hint: You should have enough hints to find the files, don't run a brute forcer.
# Solution
`How` と `What` の2つのタブがあるだけのシンプルなサイト。タブを切り替えても、特に何も変化はない。ので、レスポンスを確認。すると、このサイトは `index.html` , `mycss.css` , `myjs.js` で構成されている事がわかった。

### index.html
```HTML:index.html
<!doctype html>
<html>
  <head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
		<h1>Just some boring HTML</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">What</button>

      <div id="tabintro" class="tabcontent">
		<h3>How</h3>
		<p>How do you like my website?</p>
      </div>

      <div id="tababout" class="tabcontent">
		<h3>What</h3>
		<p>I used these to make this site: <br/>
		  HTML <br/>
		  CSS <br/>
		  JS (JavaScript)
		</p>
	<!-- Here's the first part of the flag: picoCTF{t -->
      </div>

    </div>

  </body>
</html>

```
コメントされている部分にフラグの初めが書いてある。`the first part of the flag` と書かれているので、残りのファイルを見てみる。

### mycss.css
```CSS:mycss.css
div.container {
    width: 100%;
}

header {
    background-color: black;
    padding: 1em;
    color: white;
    clear: left;
    text-align: center;
}

body {
    font-family: Roboto;
}

h1 {
    color: white;
}

p {
    font-family: "Open Sans";
}

.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 17px;
    width: 50%;
}

.tablink:hover {
    background-color: #777;
}

.tabcontent {
    color: #111;
    display: none;
    padding: 50px;
    text-align: center;
}

#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```
コメントされている部分にフラグに関する事が書かれている。

### myjs.js
```JavaScript:myjs.js
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
	tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
	tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
	elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */

```
`How can I keep Google from indexing my website?` ... ほえ？これで終わりじゃないんかい...\
Googleがサイトをクロールする際にみるのは、`robots.txt` が考えられる。そこで`/robots.txt` にアクセスすると、
```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```
が表示され、3つ目の情報を入手。
次は、Apache Server に関する何かしらのファイルにアクセスしたらいいっぽい。色々調べてみると `.htaccess` というファイルの存在に遭遇。このファイルは、Apacheでのみ使用可能なWebサーバー設定ファイルである。てことで、`/.htaccess` にアクセス。
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
うおおおお...4つ目の情報ゲット。まだ続いてて草。\
mac専用？のファイルのことを述べているみたいだが、調べてみても名前がわからず断念(探し方が悪かったかも)。[writeup](https://zenn.dev/felvi/articles/7f3e2e22498cff#scavenger-hunt-(50pts))を読んでみると、正解は `.DS_Store` 。見たことある。macで自動生成されるシステムファイルらしい。`/.DS_Store` にアクセスして、最後の情報を入手した。
```
Congrats! You completed the scavenger hunt. Part 5: _a69684fd}
```

# Reference
- https://zenn.dev/felvi/articles/7f3e2e22498cff#scavenger-hunt-(50pts)