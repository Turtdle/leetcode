# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        old = -1
        bot = 0
        top = n
        check = n//2
        while old != check:
            old = check
            if(isBadVersion(check)):
                top = check
                check = (top+bot)//2
            if(not isBadVersion(check)):
                bot = check
                check = (top+bot)//2
            

        return old+1
