def majorityElement(self, nums: List[int]) -> int:
    #linear time, constant space
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        