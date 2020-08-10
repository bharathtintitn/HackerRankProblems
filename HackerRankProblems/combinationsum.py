import pdb
from collections import defaultdict

class Solution(object):

    def combinationSum4(self, nums, target):

        mem = defaultdict(bool)
        self.count = 0
        def dp(nums, total, mem, res):
            #pdb.set_trace()
            if total == target:
                mem[tuple(res)] = True
                print "************"
                self.count += 1
                return 1
            if mem[tuple(res)]:
                return 0

            if total > target:
                return 0

            print "mem:", mem
            ret = 0
            for i in xrange(len(nums)):
                if total + nums[i] <= target:
                    ret = dp(nums, total+nums[i], mem, res+[nums[i]])
            mem[tuple(res)] = True
            return ret

        dp(nums, 0, mem, [])
        return self.count

a = Solution()
#print a.combinationSum4([1, 2, 3], 4)
print a.combinationSum4([4,2,1], 32)
