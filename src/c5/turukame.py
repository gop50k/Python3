# coding: UTF-8
# 鶴亀算を行うプログラム

class Turu:
    def get_name(self):
        return '鶴'
    def get_regs(self):
        return 2

class Kame:
    def get_name(self):
        return '亀'
    def get_regs(self):
        return 4

class Tako:
    def get_name(self):
        return 'タコ'
    def get_regs(self):
        return 8

class Ika:
    def get_name(self):
        return 'イカ'
    def get_regs(self):
        return 10

def calc_turukame(turu, kame, heads, legs):
    turu_1 = turu.get_regs()
    kame_1 = kame.get_regs()
    turu_name = turu.get_name()
    kame_name = kame.get_name()

    kame_num = (legs - (turu_1 * heads)) // (kame_1 - turu_1)
    turu_num = heads - kame_num
    print('---')
    print('頭 = ', heads, '足 = ', legs)
    print(turu_name, '=', turu_num)
    print(kame_name, '=', kame_num)
    return (turu_num, kame_num)

if __name__ == '__main__':
    calc_turukame(Turu(), Kame(), heads = 10, legs = 28)
    calc_turukame(Tako(), Ika(), heads = 11, legs = 100)
