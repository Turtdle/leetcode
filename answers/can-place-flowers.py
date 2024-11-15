class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index in range(len(flowerbed)):
            prev = index - 1 if index > 0 else 0
            nex = index + 1 if index < len(flowerbed) - 1 else  len(flowerbed)-1
            if flowerbed[prev] == 0 and flowerbed[nex] == 0 and flowerbed[index] == 0:
                flowerbed[index] = 1
                n -= 1
        return True if n <= 0 else False
