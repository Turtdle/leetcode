class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window = []
        output = []
        if len(nums) < (k*2)+1:
            return [-1] * len(nums)
        window_size = (k*2)+1
        total = 0
        for i in range(len(nums)):
            if i < k:
                output.append(-1)
            window.append(nums[i])
            total += nums[i]
            if len(window) == window_size:
                output.append(total//window_size)
                total -= window[0]
                window.pop(0)
                
        return output + [-1] * k
        #bruh
