"""
@Project: LeetCode   
@Description: LeetCode-387-字符串中第一个唯一字符
@Time:2021/6/10 14:59       
@Author:zexin                
 
"""
from collections import Counter

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 统计频数，返回第一个频数1的字符的下标
        # 用时：80ms/94.59%; 内存：15.3M/15.07%
        co = dict(Counter(list(s)))
        print(co)
        res_list = []
        for key in co:
            if co[key] == 1:
                res_list.append(key)
        if res_list:
            return s.index(res_list[0])
        else:
            return -1

so = Solution()
print(so.firstUniqChar("agdjkasgdjkahdajkhdkajsbn"))