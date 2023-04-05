"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
from typing import List
def find_maximal_subarray_sum(nums: List[int], k: int) -> List:
    """
    :param nums: sequense
    :param k: number of numbers
    :return: summ of k numbers in nums
    """
    """
    result = 0
    while k>0:
        Max = max(nums)
        result = result+Max
        nums.remove(Max)
        k-=1
    return result
    """
    tmp_max = min(nums)
    tmp_list=[]
    for k in range(len(nums)):
        for i in range(len(nums)-k+1):
            tmp_sum = sum(nums[i:i+k])
            if tmp_sum > tmp_max:
                tmp_max = tmp_sum
                tmp_list = nums[i:i+k]
    return tmp_list
print(*find_maximal_subarray_sum(nums,k))
