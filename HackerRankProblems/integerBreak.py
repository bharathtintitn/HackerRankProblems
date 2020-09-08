'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Ex 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Ex 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

import pdb

class Solution:
	def integerBreak(self, n: int) -> int:
		if n <= 1:
			return n
		if n == 2:
			return 1
		if n == 3:
			return 2

		prod = 1
		while n > 4:
			prod *= 3
			n = n - 3
		prod *= n
		print(prod)
		return prod


a = Solution()
assert a.integerBreak(2) == 1
assert a.integerBreak(10) == 36
assert a.integerBreak(15) == 243
