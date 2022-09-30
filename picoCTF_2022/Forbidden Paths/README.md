# [Web] Forbidden Paths 200pts
Can you get the flag?
Here's the [website](http://saturn.picoctf.net:55827/).
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

# Solution
問題文にフラグの存在場所が書いてある。サイトを見ると、指定したファイルを表示することができる。従って, `../../../../flag.txt` を送信することでフラグを得ることができる。ちなみに、txtファイルだけでなく、`read.php` を表示することも可能。