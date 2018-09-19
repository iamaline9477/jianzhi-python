#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

思路：
1、滑动窗口
初始化small=1，big=2;
small到big序列和小于sum，big++;大于sum，small++;
当small>big时停止
2、数学公式入手的分析'''

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        small=1
        big=2
        res=[]
        while small<big:
            count=(big+small)*(big-small+1)/2 #求和公式
            if count==tsum:
                res1=[]
                for i in range(small,big+1):
                    res1.append(i)
                res.append(res1)
                big+=1
            if count<tsum:
                big+=1
            if count>tsum:
                small+=1
        return res


#n为奇数时，序列中间的数正好是序列的平均值，所以条件为：n % 2 == 1 && sum % n == 0；
#n为偶数时，序列中间两个数的平均值是序列的平均值，而这个平均值的小数部分为0.5，所以条件为：(sum % n) * 2 == n
#S = (1 + n) * n / 2 得到 n<=sqrt(2S)
#故将n从2至sqrt(2S)遍历寻找即可
#n确定后，对应的起始值k=(sum / n) - (n - 1) / 2，其中sum/n为中间值
# import math
# class Solution:
#     def FindContinuousSequence(self, tsum):
#         res=[]
#         n=int(math.sqrt(2*tsum))
#         while n>=2:
#             if (n%2==1 and tsum%n==0) or (tsum%n)*2==n:
#                 k=int((tsum/n)-(n-1)/2)
#                 res1=[]
#                 for i in range(n):
#                     res1.append(k)
#                     k+=1
#                 res.append(res1)
#             n-=1
#         return res