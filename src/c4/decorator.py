# coding: UTF-8
# デコレータを試すプログラム

def show_func_name(func):
    def wrapper(*args, **kwargs):
        print('---- start : ' + func.__name__)
        res = func(*args, **kwargs)
        print('---- end : ' + func.__name__)
        return res
    return wrapper

@show_func_name
def kakugen1():
    print('賢い人間の静かな叫びは')
    print('愚かな人間の叫びより聞かれる')

@show_func_name
def kakugen2():
    print('求め続けよ。さすれば与えられん。')

kakugen1()
kakugen2()
