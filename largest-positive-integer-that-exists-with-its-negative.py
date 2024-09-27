"""
Given an integer array nums that does not contain any zeros, 
find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""

def findMaxK(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)-1, -1, -1):
        if -nums[i] in nums:
            return nums[i]
    return -1

