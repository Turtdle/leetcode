from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        index1 = 0
        index2 = 0
        output = []
        while index1 != len(nums1) or index2 != len(nums2):
            if index1 == len(nums1):
                output.append(nums2[index2])
                index2 += 1
            elif index2 == len(nums2):
                output.append(nums1[index1])
                index1 += 1
            elif nums1[index1][0] < nums2[index2][0]:
                output.append(nums1[index1])
                index1 += 1
            elif nums2[index2][0] < nums1[index1][0]:
                output.append(nums2[index2])
                index2 += 1
            else:
                output.append([nums2[index2][0], nums2[index2][1] + nums1[index1][1]])
                index1 += 1
                index2 += 1
        return output

if __name__ == "__main__":
    s = Solution()
    print(s.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
            
