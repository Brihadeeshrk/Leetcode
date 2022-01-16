'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Resultant list
        quadruplets = list()
        # Base condition
        if nums is None or len(nums) < 4:
            return quadruplets
        # Sort the array
        nums.sort()
        # Length of the array
        n = len(nums)
        # Loop for each element of the array
        for i in range(0, n - 3):
            # Check for skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Reducing to three sum problem
            for j in range(i + 1, n - 2):
                # Check for skipping duplicates
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Left and right pointers
                k = j + 1
                l = n - 1
                # Reducing to two sum problem
                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if current_sum < target:
                        k += 1
                    elif current_sum > target:
                        l -= 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return quadruplets