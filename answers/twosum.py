def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []

def main():
    print(twoSum(nums=[2,7,11,15], target=9))

if __name__ == "__main__":
    main()