def searchInsert(nums: list[int], target: int) -> int:
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    if target == nums[0]:
        return 0
    top = len(nums) - 1
    bottom = nums[0]
    while bottom <= top:
        mid = (top + bottom) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            bottom = mid + 1
        else:
            top = mid - 1
    
    return bottom