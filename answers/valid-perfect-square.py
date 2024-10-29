class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        oldmid = -1
        top = num
        bot = 1
        mid = top//2
        if num == 1:
            return True
        if mid == 0:
            return False

        
        while num / mid != mid:
            print(f'mid: {mid}')
            print(f'top: {top}')
            print(f'bot: {bot}')
            if num / mid == mid:
                return True
            if num // mid < mid:
                top = mid
                mid = (bot + mid)//2 
            if num // mid > mid:
                bot = mid
                mid = (top + mid)//2
            if mid == oldmid:
                return False
            oldmid = mid
            if mid == 0:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(5))