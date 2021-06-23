"""
@Project: LeetCode   
@Description: LeetCode-389-找不同
@Time:2021/6/15 11:26       
@Author:zexin                
 
"""
from collections import Counter

"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：

输入：s = "", t = "y"
输出："y"
示例 3：

输入：s = "a", t = "aa"
输出："a"
示例 4：

输入：s = "ae", t = "aea"
输出："a"

"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 求频数集合，先比较key值，再比较频数，返回差异的key值
        # 用时：44ms/68.74%; 内存：14.8M/90.42%
        co_s = Counter(s)
        co_t = Counter(t)
        for key in co_t:
            if co_t[key] != co_s[key]:
                return key

so = Solution()
print(so.findTheDifference("ae", "eaa"))