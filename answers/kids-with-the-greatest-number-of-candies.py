class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        m = max(candies)
        for kid in candies:
            if kid + extraCandies >= m:
                out.append(True)
            else:
                out.append(False)
        return out
