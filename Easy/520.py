"""
@Project: LeetCode   
@Description: LeetCode-520-检测大写字母
@Time:2021/6/8 11:42       
@Author:zexin                
 
"""
"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 暴力遍历
        # 用时：48ms/19.54%; 内存：14.9M/28.28%
        big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        word_list = list(word)
        word_len = len(word)
        if word_len <= 1:
            return True
        else:
            if word_list[0] in big:
                if word_list[1] in big:
                    for i in range(2, word_len):
                        if word_list[i] not in big:
                            return False
                else:
                    for i in range(1, word_len):
                        if word_list[i] in big:
                            return False
            else:
                for i in range(1, word_len):
                    if word_list[i] in big:
                        return False
            return True

    def detectCapitalUse1(self, word: str) -> bool:
        # 字符串判断函数：
        # 用时：36ms/87.40%; 内存：14.9M/23.27%
        return word.isupper() or word.islower() or word.istitle()


so = Solution()
if so.detectCapitalUse('woSHni'):
    print(1)
else:
    print(0)