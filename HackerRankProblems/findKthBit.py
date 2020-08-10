'''
Given two positive integers n and k, the binary string  Sn is formed as follows:

S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".

'''

class Solution(object):

    def findKthBit(self, n, k):
	'''Return k index in string.
           Since n is very small we can concatenate string.
	'''
        s = '0'
        for i in xrange(n-1):
            add = "".join(map(lambda x: '0' if x == '1' else '1', s[::-1]))
            s = s + '1' + add
            #print s
        return s[k-1]

a = Solution()
assert a.findKthBit(3, 1) == '0'
assert a.findKthBit(4, 11) == '1'
assert a.findKthBit(1, 1) == '0'
assert a.findKthBit(2, 3) == '1'
