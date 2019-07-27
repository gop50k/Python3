# coding: UTF-8
# 集合型(set)を試す,基本的にキー；値の感じでいける。名前；点数の辞書型を利用して平均点を出すPG

# 成績データを辞書型で算出
records = {
    'Tanaka':72, 'Kawada':65,
    'Sakea':100, 'Kuramnoto':56,
    'Onaka':66, 'Akashi':80, 'Kuchinashi':89
}

# 合計点を求める
sum_v = 0
for v in records.values():
    sum_v += v

# 平均点を求める
ave_v = sum_v / len(records)
print('SumPoint', sum_v)
print('AveragePoint', ave_v)

# 平均定位を算出すると共にフォーマットの指定
fmt = '| {0:<7} | {1:>4} | {2:>5} '
print('| Name | Point | DiffToAverage ')
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める
    diff_v = round(diff_v, 1)
    # 書式に沿って出力
    print(fmt.format(name, v, diff_v))
