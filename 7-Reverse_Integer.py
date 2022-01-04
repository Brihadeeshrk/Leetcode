'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''


class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        reversedNumber = 0
        while x:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10
        if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:
            return 0
        return -reversedNumber if isNegative else reversedNumber
