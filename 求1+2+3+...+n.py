#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

思路：
递归+短路求值'''


class Solution:
    def Sum_Solution(self, n):
        ans = n
        temp = ans and self.Sum_Solution(n-1)
        ans +=temp
        return