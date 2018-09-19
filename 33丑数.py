#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：
1、判断丑数：除以2 直到无法整除then除以3直到无法整除then除以5直到无法整除 余数为0则为丑数
2、丑数的生成：对现有的丑数列表里各数，min(num*2,num*3,num*5) 注意有可能重复'''


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=0:
            return 0
        a=[1]
        index2=0
        index3=0
        index5=0
        while len(a)<index:
            val=min(a[index2]*2,a[index3]*3,a[index5]*5)
            if val==a[index2]*2:
                index2+=1
            if val==a[index3]*3:   #注意不能用elif 因为有的数可能包含2.3.5中不止一个因子，对应index都需要变化
                index3+=1
            if val==a[index5]*5:
                index5+=1
            a.append(val)
        return a[index-1]