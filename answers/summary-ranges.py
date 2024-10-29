def summaryRanges(nums: List[int]) -> List[str]:
    #take two pointers of the array and if the next element is + 1 of prev then we move the small array up one size
    #then if it isnt then we can add the small array to a return array and start over at the new pos
    if not nums:
        return []
    res = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            res.append(str(start) + "->" + str(nums[i-1]) if start != nums[i-1] else str(start))
            start = nums[i]
    res.append(str(start) + "->" + str(nums[-1]) if start != nums[-1] else str(start))
    return res