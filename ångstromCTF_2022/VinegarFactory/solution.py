import string
import re
import pexpect
import sys

# アルファベットの小文字 abcdefghijklmnopqrstuvwxyz
alpha = string.ascii_lowercase

# 暗号用の関数
def encrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(key[i]) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

# 復号用の関数
def decrypt(ret, key):
    msg = ""
    i = 0
    for c in ret:
        if c in alpha:
            if alpha.index(c) - alpha.index(key[i]) >= 0:
                msg += alpha[alpha.index(c) - alpha.index(key[i])]
                i = (i + 1) % len(key)
            else:
                msg += alpha[len(alpha) + alpha.index(c) - alpha.index(key[i])]
                i = (i + 1) % len(key)
        else:
            msg += c
    return msg

# key 候補を見つける関数
def searchKey(before, after):
    key = ""
    for c in alpha:
        if after == encrypt(before, c):
            key = c
            break
    return key

# actf{---} の形を見つけ出す関数
def searchFlagFormat(text, start):
    frontKakkoIndex = 0
    backKakkoIndex = 0
    for index in range(start, len(text)):
        # { ----- } の箇所を探す
        if text[index] == '{':
            frontKakkoIndex = index
        elif text[index] == '}' and frontKakkoIndex != 0:
            backKakkoIndex = index
        # 候補を見つけたら、return
        if frontKakkoIndex != 0 and backKakkoIndex != 0:
            if 50 >= backKakkoIndex - frontKakkoIndex - 1 >= 10:
                break
            else:
                frontKakkoIndex = 0
                backKakkoIndex = 0
    return [frontKakkoIndex, backKakkoIndex]

# fleg を見つけ出す関数
def getFleg(text):
    index = 0
    fleg = ""
    pattern = [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]
    while index < len(text):
        indexList = searchFlagFormat(text, index)
        index = indexList[1] + 1

        if indexList[1] == 0:
            break

        if indexList[0] - 4 >= 0 and indexList[1] + 5 <= len(text):
            front = text[indexList[0] - 4: indexList[0]]
            back = text[indexList[1] + 1 :indexList[1] + 5]
            frontCount = 0
            backCount = 0
            for f in front:
                if f in alpha:
                    frontCount += 1
            for b in back:
                if b in alpha:
                    backCount += 1
            if frontCount == 4 and backCount == 4:
                key = searchKey('a', text[indexList[0] - 4]) + searchKey('c', text[indexList[0] - 3]) + searchKey('t', text[indexList[0] - 2]) + searchKey('f', text[indexList[0] - 1])
                for p in pattern:
                    msg = decrypt(text, key[p[0]] + key[p[1]] + key[p[2]] + key[p[3]])
                    if ('actf{' in msg) and ('}fleg' in msg):
                        fleg = re.search('actf{(.+?)}fleg', msg).group(1)

    return "actf{" + fleg + "}"

# Pexpectを用いて実際にフラグを得る
# 参考 https://takuya-1st.hatenablog.jp/entry/2016/06/16/000000
#     https://pexpect.readthedocs.io/en/stable/api/pexpect.html
connect = pexpect.spawn("nc challs.actf.co 31333", encoding="utf-8")      # コマンド開始
connect.logfile = sys.stdout                                              # 出力結果表示
count = 0
while count < 50:
    count += 1
    connect.expect(">")                                                   # 入力画面を示す > が出てくるまで待機
    resultFleg = getFleg(connect.before)
    connect.sendline(resultFleg)                                          # Fleg送信
    if count == 50:
        break
connect.expect(pexpect.EOF)                                               # 接続終了