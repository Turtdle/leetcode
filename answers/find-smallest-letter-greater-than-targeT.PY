from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        #cool ass solution
        return letters[left % len(letters)]
            
        
def main():
    testcase = ["c", "f", "j"]
    target = "c"
    s = Solution()
    print(s.nextGreatestLetter(testcase, target))

if __name__ == "__main__":
    main()