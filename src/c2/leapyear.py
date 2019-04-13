# coding: UTF-8
# 閏年判定プログラム
year = int(input("西暦何年？"))

is_leap = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0 ))

if is_leap:
    print("閏年です。")

else:
    print("平年です。")
