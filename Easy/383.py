"""
@Project: pythonProject   
@Description: LeetCode-383-赎金信
@Time:2021/6/4 13:55       
@Author:zexin                
 
"""
from collections import Counter

"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)


示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true

提示：

你可以假设两个字符串均只含有小写字母。
"""


class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        # 暴力求解，在杂志中寻找各个赎金信字符，找到后从杂志中删除该字符
        # 用时：72ms/57.23%; 内存：15.2M/12.81%
        ransomList = list(ransomNote)
        magazineList = list(magazine)
        flag = 0
        for r_cha in ransomList:
            for m_cha in magazineList:
                if r_cha == m_cha:
                    magazineList.remove(m_cha)
                    flag += 1
                    break
            if flag == 0:
                return False
            else:
                flag = 0
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        # 不用==判断，用in
        # 用时：60ms/79.70%; 内存：15.3M/10.26%
        ransomList = list(ransomNote)
        magazineList = list(magazine)
        for r_char in ransomList:
            if r_char in magazineList:
                magazineList.remove(r_char)
            else:
                return False
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        # 使用Counter函数,统计字符串中字符出现的频数，在做比较
        # 用时：56ms/86.22%; 内存：15.1M/58.73%
        c_ran = Counter(ransomNote)
        c_mag = Counter(magazine)
        for key in c_ran:
            if key not in c_mag:
                return False
            else:
                if c_ran[key]>c_mag[key]:
                    return False
        return True


so = Solution()
if so.canConstruct3("sjswbw", "hajsdswklabjw"):
    print("True")
else:
    print("False")

