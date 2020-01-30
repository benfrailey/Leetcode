import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        target = size / 2
        if target < 1:
            if not nums1:
                return nums2[0]
            else:
                return nums1[0]
        target = math.ceil(target)



        i = 0
        j = 0
        k = 0
        nums3 = []
        while k < target + 1:
            if i >= len(nums1):
                nums3.append(nums2[j])
                j = j + 1
                k = k + 1
                continue

            if j >= len(nums2):
                nums3.append(nums1[i])
                i = i + 1
                k = k + 1
                continue

            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
                k = k + 1
            else:
                nums3.append(nums2[j])
                j = j + 1
                k = k + 1

        if size % 2 == 0:
            num = (nums3[target - 1] + nums3[target]) / 2
            return num
        else:
            return nums3[target - 1]
        
