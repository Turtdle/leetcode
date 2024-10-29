def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    ar3 = merge_arrays(nums1, nums2)
    n = len(ar3)
    if n % 2 == 0:
        return (ar3[n // 2 - 1] + ar3[n // 2]) / 2
    else:
        return ar3[n // 2]
def merge_arrays(ar1, ar2):
    i = 0
    j = 0
    k = 0
    n1 = len(ar1)
    n2 = len(ar2)
    ar3 = []

    while i < n1 and j < n2:
      
        # Pick smaller of the two current elements and move ahead in the array of the picked element
        if ar1[i] < ar2[j]:
            ar3.append(ar1[i])
            i += 1
        else:
            ar3.append(ar2[j])
            j += 1

    # if there are remaining elements of the first array, move them
    while i < n1:
        ar3.append(ar1[i])
        i += 1

    # Else if there are remaining elements of the second array, move them
    while j < n2:
        ar3.append(ar2[j])
        j += 1

    return ar3