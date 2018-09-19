#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

思路：
依次判断'''

class Solution:
    # s字符串
    def isNumeric(self, s):
        a=['0','1','2','3','4','5','6','7','8','9']
        if not s or s in a:
            return True
        elif len(s)>1 and ((s[0]=='+' and s[1]!='-') or (s[0]=='-' and s[1]!='+')):
            return self.isNumeric(s[1:])
        elif ('+' in s or '-' in s) and 'e' not in s and 'E' not in s:
            return False
        elif 'e' in s:
            idx=s.index('e')
            if not s[0:idx] or not s[idx+1:] or ('e'in s[0:idx]) or ('E'in s[0:idx]) or ('e'in s[idx+1:]) or ('E'in s[idx+1:]) or ('.'in s[idx+1:]):
                return False
            else:
                return self.isNumeric(s[0:idx]) and self.isNumeric(s[idx+1:])
        elif 'E' in s:
            idx = s.index('E')
            if not s[0:idx] or not s[idx + 1:] or ('e'in s[0:idx]) or ('E'in s[0:idx]) or ('e'in s[idx+1:]) or ('E'in s[idx+1:]) or ('.'in s[idx+1:]):
                return False
            else:
                return self.isNumeric(s[0:idx]) and self.isNumeric(s[idx + 1:])
        elif '.' in s:
            idx=s.index('.')
            if not s[idx+1:] or ('e'in s[0:idx]) or ('E'in s[0:idx]) or ('.'in s[0:idx]) or ('e'in s[idx+1:]) or ('E'in s[idx+1:]) or ('.'in s[idx+1:]):
                return False
            else:
                return self.isNumeric(s[0:idx]) and self.isNumeric(s[idx+1:])
        elif len(s)>1 and s[0] in a:
            return self.isNumeric(s[1:])
        else:
            return False

#way2:
# class Solution:
    # # s字符串
    # def isNumeric(self, s):
    #     hasE,hasPoint,hasSymbol=False,False,False
    #     for i in range(len(s)):
    #         if s[i]=='E' or s[i]=='e':
    #             if i==len(s)-1:
    #                 return False
    #             if hasE==True:
    #                 return False
    #             hasE=True
    #         elif s[i]=='+' or s[i]=='-':
    #             if hasSymbol and s[i-1]!='e' and s[i-1]!='E':
    #                 return False
    #             if not hasSymbol and i>0 and s[i-1]!='e' and s[i-1]!='E':
    #                 return False
    #             hasSymbol=True
    #         elif s[i]=='.':
    #             if hasE or hasPoint:
    #                 return False
    #             hasPoint=True
    #         elif ord(s[i])>ord('9') or ord(s[i])<ord('0'):
    #             return False
    #     return True