#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。

思路：
从矩阵第一排最右元素开始查找，若找到则返回，
若该元素较大则与其左边的元素继续比较，
若该元素较小则与下面的元素继续比较'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not target or not array:
            return False
        m=0
        n=len(array[0])-1
        while m<=len(array)-1 and n>=0:
            if array[m][n]==target:
                return True
            elif array[m][n]<target:
                m+=1
            elif array[m][n]>target:
                n-=1
        return False

