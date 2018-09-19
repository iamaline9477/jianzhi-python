#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路：
二分法，数组实际上分为两个递增子数组，
设置头、尾、中间的指针，依次比较大小确定范围，
若中间点大于头则它位于前一个递增子数组， 令new头=中间
若中间点小于尾则它位于后一个递增子数组，令new尾=中间
注意三者相等时需要暴力求解，如{1,0,1,1,1}'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        head=0
        tail=len(rotateArray)-1
        while rotateArray[head]>=rotateArray[tail]:
            if tail-head==1:
                return rotateArray[tail]
            mid=(head+tail)//2
            if rotateArray[head]==rotateArray[tail]==rotateArray[mid]: #暴力求解
                return min(rotateArray)
            elif rotateArray[head]<=rotateArray[mid]:
                head=mid
            elif rotateArray[tail]>=rotateArray[mid]:
                tail=mid
