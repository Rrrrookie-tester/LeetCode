"""
@Project: pythonProject   
@Description: LeetCode-349-两个数组的交集
@Time:2021/6/5 9:58       
@Author:zexin                
 
"""
from typing import List

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 直接求解，当nums1中元素在nums2中时，放入结果集（结果集要去重）
        # 用时：68ms/15.27%; 内存：14.9M/82.25%
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
        return res

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用集合的交集运算
        # 用时：44ms/70.14%; 内存：14.8M/87.94%
        return list(set(nums1).intersection(set(nums2)))

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 去重后使用位运算符
        # 用时：28ms/99.63%; 内存：14.8M/96.89%
        return list(set(nums1) & set(nums2))


so = Solution()
print(so.intersection3([1, 2, 2, 1], [2, 2]))