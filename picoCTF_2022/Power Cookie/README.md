# [Web] Power Cookie 200pts
Can you get the flag?
Go to this [website](http://saturn.picoctf.net:61304/) and see what you can discover.

# Solution
Cookie問題。`guest.js`をみてみる。
```JS
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```
`isAdmin=1`に変更することでフラグを入手できる。