"""
@Project: LeetCode   
@Description: LeetCode-409-最长回文串
@Time:2021/6/15 11:50       
@Author:zexin                
 
"""
from collections import Counter

"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 得到频数表，根据频数表判断
        # 用时：40ms/78.70%; 内存：14.7M/95.24%
        co_s = Counter(s)
        res = 0
        flag = 0
        for key in co_s:
            shang, yu = divmod(co_s[key], 2)
            res = res + 2 * shang
            if co_s[key] % 2 == 1:
                flag = 1
        if flag == 1:
            return res + 1
        else:
            return res


so = Solution()
print(so.longestPalindrome("abcdcbas"))
