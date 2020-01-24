# coding: UTF-8
# 鶴亀算のユニットテスト

import unittest, turukame

class TestTurukame(unittest.TestCase):
    def test_turukame(self):
        turu, kame = turukame.calc_turukame(
            turukame.Turu(),
            turukame.Kame(),
            heads=10, legs=28
        )

        self.assertEqual(turu, 6)
        self.assertEqual(kame, 4)
