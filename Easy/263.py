"""
@Project: pythonProject   
@Description: LeetCode-263-丑数
@Time:2021/6/5 15:52       
@Author:zexin                
 
"""
"""
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数2、3 和/或5的正整数。

示例 1：

输入：n = 6
输出：true
解释：6 = 2 × 3
示例 2：

输入：n = 8
输出：true
解释：8 = 2 × 2 × 2
示例 3：

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。
示例 4：

输入：n = 1
输出：true
解释：1 通常被视为丑数。

"""


class Solution:
    def isUgly(self, n: int) -> bool:
        # 递归，尝试整除2 3 5，可以整除的话将结果再次进行计算，直到不满足
        # 用时：25ms/10.44%; 内存：14.9M,19.17%
        global res
        if n == 1:
            res = True
        elif n % 2 == 0:
            n = n // 2
            self.isUgly(n)
        elif n % 3 == 0:
            n = n // 3
            self.isUgly(n)
        elif n % 5 == 0:
            n = n // 5
            self.isUgly(n)
        elif n % 2 != 0 or n % 3 != 0 or n % 5 != 0:
            res = False
        return res




so = Solution()
if so.isUgly(6):
    print("True")
else:
    print("False")
