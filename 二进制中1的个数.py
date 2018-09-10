#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路：
一：如果用s.count('1')则负数不符合要求，需要提前转换负数的形式
二：用按位与 & n-1 多次操作，每次操作会消除最末尾的1，消除的次数即为1的个数'''

class Solution:
    def NumberOf1(self, n):
        ret=0
        if n<0:
            n = n & 0xffffffff #负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
        while n:
            n = n & n-1
            ret +=1
        return ret