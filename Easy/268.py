"""
@Project: pythonProject   
@Description: LeetCode-268-缺失的数字
@Time:2021/6/5 13:55       
@Author:zexin                
 
"""
from typing import List

"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

进阶：

你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 排序后直接遍历
        # 用时：64ms/27.16%; 内存：15.8M/35.98%
        nums.sort()
        if nums[-1] == len(nums)-1:
            return len(nums)
        elif nums[0] != 0:
            return 0
        else:
            for i in range(0, len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    return nums[i]+1

    def missingNumber(self, nums: List[int]) -> int:
        # 数学方法，假定不缺少数字，求和，再将已有的数字求和，差值为缺少的数字
        # 用时：36ms/98.35%; 内存：15.7M/54.53%
        res = 0
        n = len(nums)
        for i in nums:
            res = res + i
        return int((n*(n+1))/2 - res)


so = Solution()
print(so.missingNumber([9,6,4,2,3,5,7,0,1]))