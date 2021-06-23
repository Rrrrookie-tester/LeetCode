"""
@Project: LeetCode   
@Description: LeetCode-504-7进制数
@Time:2021/6/9 15:36       
@Author:zexin                
 
"""
"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是[-1e7, 1e7] 。

"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        # 暴力节，取商和余数拼接
        # 用时：44ms/34.49%; 内存：14.8/49%
        if num == 0:
            return "0"
        elif num < 0:
            num = -num
            t = divmod(num, 7)
            a = t[0]
            b = str(t[1])
            while a >= 7:
                b = str(divmod(a, 7)[1]) + str(b)
                a = divmod(a, 7)[0]
            return '-' + ((str(a) + b).lstrip('0'))
        else:
            t = divmod(num, 7)
            a = t[0]
            b = str(t[1])
            while a >= 7:
                b = str(divmod(a, 7)[1]) + str(b)
                a = divmod(a, 7)[0]
            return (str(a)+b).lstrip('0')


so = Solution()
print(so.convertToBase7(-7))


