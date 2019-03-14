#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

题目描述：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路：
 - 由右上角至左下角进行查找；
 - 若当前元素值大于目标值，则向左继续查找；若当前元素值小于目标值，则向下继续查找；否则返回True；
 - 若到达最左或最下方时仍未找到，则返回False

#运行时间：294ms
#占用内存：5624k
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not target or not array:
            return False
        row=len(array)
        col=len(array[0])
        m=0
        n=col-1
        while m<=row-1 and n>=0:
            if array[m][n]>target:
                n-=1
            elif array[m][n]<target:
                m+=1
            else:
                return True
        return False

