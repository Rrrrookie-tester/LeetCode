"""
@Project: LeetCode   
@Description: LeetCode-414-第三大的数
@Time:2021/6/15 16:14       
@Author:zexin                
 
"""
from typing import List

"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

 

示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。

"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 去重后排序，根据长度确定返回
        # 用时：40ms/74.82%; 内存：15.7M/58.39%
        new_nums = list(set(nums))
        new_nums.sort(reverse=True)
        if len(new_nums)<3:
            return new_nums[0]
        return new_nums[2]


so = Solution()
print(so.thirdMax([2, 2, 3, 1]))