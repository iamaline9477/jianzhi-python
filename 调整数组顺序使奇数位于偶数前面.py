#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个整数数组，
实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路：
依次判断奇偶数，奇数添加到空list1，偶数添加到空list2，再合并'''

class Solution:
    def reOrderArray(self, array):
        a,b=[],[]
        for i in range(len(array)):
            a.append(array[i]) if array[i]%2!=0 else b.append(array[i])
        return a+b

# way2 lambda表达式
# class Solution:
#     def reOrderArray(self, array):
#         return sorted(array,key=lambda x:x%2,reverse=True)