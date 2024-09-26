def duplicateNumbersXOR(self, nums: list[int]) -> int:
    numss = set()
    xor = 0
    for num in nums:
        if num in numss:
            xor ^= num
        else:
            numss.add(num)

    return xor