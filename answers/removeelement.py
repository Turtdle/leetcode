def removeElement(nums: list[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    
    return count

    """
    for array [3,2,2,3]
    we have count keep track of beginning 
    count is 
    [3,2,2,3]
     ^
    i is also
    [3,2,2,3]
     ^
    but if i == val then we do nothing;
    if i != val then we move count up one, and move the value at i (nums[i]) to nums[count]
    """