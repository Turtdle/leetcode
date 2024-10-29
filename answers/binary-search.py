class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        left = 0
        right = len(nums)-1
        while (nums[mid] != target):
            if target > nums[mid]:
                left = mid
                mid = left + (right-left)//2
            if target < nums[mid]:
                right = mid
                mid = (right - left)//2
            if right-left < 2 and nums[mid] != target:
                if nums[right] == target:
                    return right
                if nums[left] == target:
                    return left
                return -1
        return mid