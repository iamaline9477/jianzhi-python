#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。

思路：
递归，注意指数是负数的情况'''


class Solution:
    def Power(self, base, exponent):
        s = 1
        if exponent == 0:
            return 1
        elif exponent >= 1:
            s = base * self.Power(base, exponent - 1)
        elif exponent < 0:
            s = 1 / self.Power(base, -exponent)
        return s

