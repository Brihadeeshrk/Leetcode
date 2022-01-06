'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the given array
        nums.sort()
        # Length of the array
        n = len(nums)
        # Resultant list
        triplets = list()
        # Loop for each character in the array
        for i in range(0, n):
            # Avoid duplicates due to i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Left and right pointers
            j = i + 1
            k = n - 1
            # Loop for remaining pairs
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Avoid duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return triplets