#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
分治法，实际上也是跳台阶问题
1、若第一步先用2*1的矩形竖着覆盖，则剩下2*(n-1)大小的矩形需要覆盖
2、若第一步先用2*1的矩形横着覆盖，则必定要用两个，剩下2*(n-2)大小的矩形需要覆盖
即共f(n-1)+f(n-2)种'''

class Solution:
    def rectCover(self, number):
        list=[0,1,2]
        for i in range(3,number+1):
            list.append(list[i-1]+list[i-2])
        return list[number]