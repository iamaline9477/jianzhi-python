#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

思路：
各种排序算法（待填坑）
*基于堆排序算法，构建最大堆。时间复杂度为O(nlogk)
*如果用快速排序，时间复杂度为O(nlogn)；
*如果用冒泡排序，时间复杂度为O(n*k)'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k<=0 or k>len(tinput):
            return []
        return sorted(tinput)[:k]