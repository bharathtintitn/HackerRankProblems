import pdb
from collections import defaultdict

class Solution(object):

    def arrayPairSum(self, nums):

        freq = defaultdict(bool)
        for i in nums:
            if freq[i] is False:
               freq[i] = 1
            else:
                freq[i] += 1

        print "freq:", freq

    def twoSum(self, nums, target):

        for i in xrange(len(nums)):
            search = (target - (nums[i]))
            index = self.binarySearch(0, len(nums)-1, search, nums)
            print "Search:", search, " index:", index
            if index <> -1 and index <> i+1:
                return sorted([index, i+1])

        return [-1, -1]

    def binarySearch(self, start, end, target, nums):

        if start <= end:

            mid = (start+end)/2
            print "mid:", mid
            if nums[mid] == target:
                return mid+1
            elif nums[mid] > target:
                return self.binarySearch(start, mid-1, target, nums)
            else:
                return self.binarySearch(mid+1, end, target, nums)
        return -1

a = Solution()
print a.twoSum([2,7,11,15], 9)
print a.twoSum([2,3,4], 6)
