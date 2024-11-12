class Solution:
    def convertToBase7(self, num: int) -> str:
        while(num > 0):
            print(num)
            st = ""
            st += str(num % 7)
            num //= 7
        st += str(num)
        return st

if __name__ == "__main__":
    s = Solution()
    print(s.convertToBase7(100))