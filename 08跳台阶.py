#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

思路：
斐波那契数列的变形，初始值不同。
n级台阶跳法可以分为：
1、先跳1步，再跳剩下n-1步有f(n-1)种
2、先跳2步，再跳剩下n-1步有f(n-2)种
即共f(n-1)+f(n-2)种'''

class Solution:
    def jumpFloor(self, number):
        if not number:
            return 0
        lst=[0,1,2]
        for i in range(3,number+1):
            lst.append(lst[i-1]+lst[i-2])
        return lst[number]