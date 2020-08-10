import pdb

class Solution(object):

    def maxSubArray(self, nums):

        array = [0]

        for i in xrange(len(nums)):
            array.append(nums[i]+array[i])

        print "array:", array

a = Solution()
a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
