"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    :param nums: sequense
    :param k: number of numbers
    :return: summ of k numbers in nums
    """
    result = 0
    while k>0:
        Max = max(nums)
        result = result+Max
        nums.remove(Max)
        k-=1
    return result