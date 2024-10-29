def findLHS(nums: List[int]) -> int:
    #sliding window
    nums.sort()
    left = 0
    right = 0
    res = 0
    while right < len(nums):
        if nums[right] - nums[left] == 1:
            res = max(res, right - left + 1)
        if nums[right] - nums[left] <= 1:
            right += 1
        else:
            left += 1
    return res
    #BRUH SLIDING WINDOW APPROACH ON THIS PROBLEM IS ASS