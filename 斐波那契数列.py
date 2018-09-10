#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

思路：
初始化a,b=0,1
yield b
a,b=b,a+b
输出指定项时考虑用list'''

class Solution:
    def Fibonacci(self, n):
        list=[0,1]
        for i in range(2,n+1):
            list.append(list[i-1]+list[i-2])
        return list[n]