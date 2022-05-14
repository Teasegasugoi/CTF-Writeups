# [WEB] crumbs 50pts
Follow [the crumbs](https://crumbs.web.actf.co/).

Server: [index.js](https://files.actf.co/07899b85b650719a814695a0b6616e3b78af90d49c012f8f581b2bb699f6f547/index.js)
# Solution
初見で解けた。\
指定されたサイトにアクセスすると、`Go to 61f57d99-6d8e-4e5e-bfc1-995dc358fce7` とだけ書かれている。Go to のあとの謎の文字列は、ソースコードより `paths[req.params.slug]` を表している。この値が `flag` のとき実際にフラグが表示される。\
ソースコードの以下の部分に注目すると、
```javascript
~~~

const paths = {};
let curr = crypto.randomUUID();
let first = curr;

for (let i = 0; i < 1000; ++i) {
    paths[curr] = crypto.randomUUID();
    curr = paths[curr];
}

paths[curr] = "flag";

~~~
```
`/{Go to 以下の文字列}` にアクセス -> `/{アクセス先で得られた文字列}` にアクセス を1000回繰り返すことで正解のフラグに辿り着けることがわかる。
そこで、Pythonでurlにアクセス、文字列取得 を繰り返すコードを書いた。