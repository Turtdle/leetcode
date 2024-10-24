from typing import List

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    if not nums:
        return 0

    left = 0
    right = 0
    min_len = float('inf')
    sum_ = 0

    while right < len(nums):
        sum_ += nums[right]
        while sum_ >= target:
            min_len = min(min_len, right - left + 1)
            sum_ -= nums[left]
            left += 1
        right += 1

    return min_len if min_len != float('inf') else 0
if __name__ == "__main__":
    print(minSubArrayLen('a', 213, [12,28,83,4,25,26,25,2,25,25,25,12])) # 2