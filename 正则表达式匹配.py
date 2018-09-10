#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

思路：
分情况讨论 递归'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s and not pattern:
            return True
        elif s and not pattern:
            return False
        elif not s and pattern: # 如果s为空，而pattern不为空，则需要判断
            if len(pattern) > 1 and pattern[1] == '*': # pattern中的第二个字符为*，则pattern后移两位继续比较
                return self.match(s, pattern[2:])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
                    # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
                    # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
                    # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                    return self.match(s[1:], pattern[2:]) or self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


