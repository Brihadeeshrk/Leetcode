'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for start in range(1, 10):
            x = start
            for y in range(start + 1, 10):
                x *= 10
                x += y
                y += 1

                if x >= low and x <= high:
                    res.append(x)
                if x > high:
                    break

        return sorted(res)
