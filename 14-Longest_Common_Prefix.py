'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
         # Longest common prefix string
        lcp = ""
        # Base condition
        if strs is None or len(strs) == 0:
            return lcp
        # Find the minimum length string from the array
        minimumLength = len(strs[0])
        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))
        # Loop until the minimum length
        for i in range(0, minimumLength):
            # Get the current character from the first string
            current = strs[0][i]
            # Check if this character is found in all other strings or not
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return lcp
            lcp += current
        return lcp

