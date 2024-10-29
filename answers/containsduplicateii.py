def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i, num in enumerate(nums):
        if num in d and abs(i - d[num]) <= k:
            return True
        d[num] = i
    return False
def main():
    print(containsNearbyDuplicate(nums=[1,2,3,1], k=3)) # True
    print(containsNearbyDuplicate(nums=[1,0,1,1], k=1)) # True
    print(containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2)) # False