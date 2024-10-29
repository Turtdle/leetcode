def threeSum(nums: list[int]) -> list[list[int]]:
    outputs = []
    nums_sorted = sorted(nums)
    for i, num in enumerate(nums_sorted):
        j = len(nums_sorted) - 1
        m = j//2
        while m != j:
            if nums_sorted[m] + num + nums_sorted[j] == 0:
                outputs.append([num, nums_sorted[m], nums_sorted[j]])
                break
            elif nums_sorted[m] + num + nums_sorted[j] < 0:
                m = (m + j)//2
            else:
                j = m
                m = j//2
    return outputs
        