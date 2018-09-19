#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：
n级台阶跳法可以分为：
1、先跳1步，再跳剩下n-1步有f(n-1)种
2、先跳2步，再跳剩下n-1步有f(n-2)种
...
n-1、先跳n-2步，再跳剩下n-1步有f(2)种
n、先跳n-2步，再跳剩下n-1步有f(1)种
n+1、一次性直接跳完，1种
即共1+f(1)+f(2)+...+f(n-2)+f(n-1)种'''

class Solution:
    def jumpFloorII(self, number):
        lst=[0,1,2]
        for i in range(3,number+1):
            lst.append(sum(lst)+1)
        return lst[number]
