# coding: UTF-8
# テキストファイルの読み書きをするプログラム

file = "./mt7_7.txt"
a_file = open(file, encoding="utf-8")
s = a_file.read()
a_file.close()
print(s)
