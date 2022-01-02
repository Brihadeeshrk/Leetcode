'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        result = False
        if len(A) >= 3:
            for x in range(0, len(A)-1):
                if A[x+1] > A[x]:
                    result = True
                else:
                    break

            if result:
                for index in range(x, len(A)-1):
                    if (A[index+1] < A[index]):
                        result = True
                    else:
                        result = False
                        break

        return result