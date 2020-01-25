# coding: UTF-8
# 鶴亀算のユニットテスト(失敗版)

import unittest, turukame

class TestTurukame2(unittest.TestCase):
    def test_turukame(self):
        turu, kame = turukame.calc_turukame(
            turukame.Turu(),
            turukame.Kame(),
            heads=10, legs=28
        )

        self.assertEqual(turu, 8)
        self.assertEqual(kame, 12)
