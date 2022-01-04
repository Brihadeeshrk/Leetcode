'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

# this was my initial understanding of the code, It worked for some of the tests but it failed once the
# test values got larger
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         for i in nums2:
#             nums1.append(i)

#         nums1.sort()
#         l = len(nums1)
#         if l == 0:
#             return 0
#         if l == 1:
#             return nums1[0]
#         elif (l-1) % 2 == 0:
#             middle = int(l / 2)
#             return nums1[middle]
#         elif (l-1) % 2 != 0:
#             middle = floor(l/2)
#             nextele = middle+1
#             s = nums1[middle] + nums1[nextele]
#             return s/2
#         else:
#             return 0

# so this is the code that works
   # Check if nums1 is smaller than nums2
   # If not, then we will swap it with nums2
import sys
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Lengths of two arrays
        m = len(nums1)
        n = len(nums2)
        # Pointers for binary search
        start = 0
        end = m
        # Binary search starts from here
        while start <= end:
            # Partition indices for both the arrays
            partition_nums1 = (start + end) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1
            # Edge cases
            # If there are no elements left on the left side after partition
            maxLeftNums1 = - \
                sys.maxsize if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            # If there are no elements left on the right side after partition
            minRightNums1 = sys.maxsize if partition_nums1 == m else nums1[partition_nums1]
            # Similarly for nums2
            maxLeftNums2 = - \
                sys.maxsize if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            minRightNums2 = sys.maxsize if partition_nums2 == n else nums2[partition_nums2]
            # Check if we have found the match
            if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
                # Check if the combined array is of even/odd length
                if (m + n) % 2 == 0:
                    return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2
                else:
                    return max(maxLeftNums1, maxLeftNums2)
            # If we are too far on the right, we need to go to left side
            elif maxLeftNums1 > minRightNums2:
                end = partition_nums1 - 1
            # If we are too far on the left, we need to go to right side
            else:
                start = partition_nums1 + 1
        # If we reach here, it means the arrays are not sorted
        raise Exception("IllegalArgumentException")
