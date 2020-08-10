class Solution(object):
    def missingNumber(self, nums):

	x1 = nums[0]
	x2 = nums[1]

	for i in xrange(1, len(nums)):
		x1 = x1 ^ nums[i]
	for i in xrange(2, len(nums)+1):
		x2 = x2 ^ i

	print x1^x2

a = Solution()
a.missingNumber([3,0,1])
