#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。

思路：
前后两个指针前后移动，越远的两个数乘积越小
故输出第一组即可'''


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        small=0
        big=len(array)-1
        while big>=small:
            count=array[small]+array[big]
            if count==tsum:
                return [array[small],array[big]]
            if count>tsum:
                big-=1
            if count<tsum:
                small+=1
        return []


# python:
# def FindNumbersWithSum(self, array, tsum):
#     diff = [tsum - i for i in array]  #筛选每个数的差值
#     filter = [i for i in array if i in diff] #如果差值也在array里则存在
#     try:
#         return [filter[0], filter[-1]]
#     except:
#         return []