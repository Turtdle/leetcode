class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = nums[0]
        def get_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total
        for ele in nums:
            m = min(m, get_sum(ele))
        return m
