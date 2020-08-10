import pdb
from collections import defaultdict

class Solution(object):

    def canPartitionKSubsets(self, nums, k):

        if k==0:
            return False
        if not nums:
            return False
        if sum(nums)%k <> 0:
            return False

        taken = defaultdict(bool)
        taken = [False for i in xrange(len(nums))]
        print taken
        total = sum(nums)/k
        print "total:", total

        def back(nums, k, taken, total, tillnow):
            print "k:{}, tillnow:{}, taken:{}".format(k, tillnow, taken)
            if k == 1:
                return True

            if total == tillnow:
                return back(nums, k-1, taken, total, 0)

            for i in xrange(len(nums)):
                if not taken[i] and tillnow+nums[i] <= total:
                    taken[i] = True
                    if back(nums, k, taken, total, tillnow+nums[i]):
                        return True
                    taken[i] = False
            return False
        return back(nums, k, taken, total, 0)

a = Solution()
print a.canPartitionKSubsets( [4, 3, 2, 3, 5, 2, 1], 4)
print a.canPartitionKSubsets([1,1,1,1,1,1,1,1,1,1], 5)
