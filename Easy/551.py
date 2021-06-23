"""
@Project: LeetCode   
@Description: LeetCode-551-学生出勤记录Ⅰ
@Time:2021/6/8 16:58       
@Author:zexin                
 
"""
from collections import Counter

"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False

"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        # 使用Counter计算A的频数，在依次比较连续出现的L的个数
        # 用时：44ms/38.17%; 内存：15M/6.41%
        ls = list(s)
        co_s = Counter(ls)
        lens = len(ls)
        if co_s['A'] <= 1:
            for i in range(0, lens-2):
                if ls[i]=='L' and ls[i+1]=='L' and ls[i+2]=='L':
                    return False
            return True
        else:
            return False

    def checkRecord1(self, s: str) -> bool:
        # 使用字符串特性：子串和count
        # 用时：40ms/63.66%; 内存：14.9M/43.66%
        if s.count('A') <= 1 and 'LLL' not in s:
            return True
        else:
            return False


so = Solution()
if so.checkRecord('PPALLP'):
    print(1)
else:
    print(0)
