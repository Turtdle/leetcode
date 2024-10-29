from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsc1 = Counter(nums1)
        numsc2 = Counter(nums2)
        intersection = (numsc1 & numsc2)
        return [key for key in intersection.keys() for time in range(intersection[key])]
    