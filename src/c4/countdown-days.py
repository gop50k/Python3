# coding: UTF-8
# 東京オリンピックまでの日付を計算する

import datetime
t1 = datetime.date(2020, 7, 24)

t2 = datetime.date.today()
diff = t1 - t2

print('今日：', t2.strftime('%Y/%m/%d'))
print('開催まであと：', diff.days, '日')
