"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
"""
from typing import List
from .two_sum_core import two_sum_core

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        使用哈希表在一次遍历中找到两数之和。
        参数:
            nums   - 整数列表
            target - 目标和
        返回:
            包含两个下标的列表，满足 nums[i] + nums[j] == target
            （保证恰好有唯一解，且 i != j）
        """
        return two_sum_core(nums, target)