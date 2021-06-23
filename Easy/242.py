"""
@Project: pythonProject   
@Description: LeetCode-242-有效的字母异位词
@Time:2021/6/4 15:46       
@Author:zexin                
 
"""
from collections import Counter

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 将两个字符串转化为list之后排序进行比较，相等就返回True
        # 用时：80ms/12.54%; 内存：15.6M/19.38%
        list_s = list(s)
        list_t = list(t)
        list_t.sort()
        list_s.sort()
        if list_t == list_s:
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        # 使用Counter计算字符出现频数，频数不同则False
        # 用时：48ms/91.81%; 内存：15.1M/93.57%
        if len(s) != len(t):
            return False
        s_con = Counter(s)
        t_con = Counter(t)
        for key in s_con:
            if key not in t_con:
                return False
            else:
                if s_con[key] != t_con[key]:
                    return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        # 优化使用Counter的方法
        s_con = Counter(s)
        t_con = Counter(t)
        return s_con == t_con


so = Solution()
if so.isAnagram2("abc", "abe"):
    print("True")
else:
    print("False")