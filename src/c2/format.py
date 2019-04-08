# coding: UTF-8
# 文字列の埋め込み
per_inch = 2.54
inch = 24
cm = inch * per_inch
desc = "{0}インチ＝{1}センチ".format(inch, cm)
print(desc)

# 名前付き引数
print("私は{name}です。".format(name = "ミドリ"))

fmt = "年齢は{age}歳で、{job}をやっています。"
s = fmt.format(age = 22, job = "プログラマー")
print(s)
