# 中身が違うファイルが存在するので、それを検索するコード
# outディレクトリ内のファイルをループ
# os.listdir でディレクトリ内のファイルをループ可能
import os
files = os.listdir('./out')
f = open('./out/xxxxx.txt', 'r')
trueData = f.read()
f.close()

for filename in files:
    f = open('./out/' + filename, 'r')
    data = f.read()
    f.close()
    if data == trueData:
        continue
    else:
        print('falseData!')
        print(filename)
        print(data)