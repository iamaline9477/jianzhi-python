#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？

思路：
回溯法'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        if threshold <= 0:
            return 0
        flag = [[0] * cols for i in range(rows)]
        self.traverse(threshold, rows, cols, flag, 0, 0)
        return self.count

    def traverse(self, threshold, rows, cols, flag, i, j):
        flag[i][j] = 1
        self.count += 1
        if i + 1 <= rows - 1 and self.bitsum(i + 1) + self.bitsum(j) <= threshold and flag[i + 1][j] == 0:
            self.traverse(threshold, rows, cols, flag, i + 1, j)
        if i - 1 >= 0 and self.bitsum(i - 1) + self.bitsum(j) <= threshold and flag[i - 1][j] == 0:
            self.traverse(threshold, rows, cols, flag, i - 1, j)
        if j + 1 <= cols - 1 and self.bitsum(i) + self.bitsum(j + 1) <= threshold and flag[i][j + 1] == 0:
            self.traverse(threshold, rows, cols, flag, i, j + 1)
        if j - 1 >= 0 and self.bitsum(i) + self.bitsum(j - 1) <= threshold and flag[i][j - 1] == 0:
            self.traverse(threshold, rows, cols, flag, i, j - 1)

    def bitsum(self, n):
        a = 0
        while n / 10.0 > 0:
            a += n % 10
            n = n // 10
        return a
