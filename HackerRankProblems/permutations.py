import pdb
import copy

class Solution(object):

    def permute(self, nums):

        self.isTaken = {}
        self.result = []
        for i in nums:
            self.isTaken[i] = False
        pdb.set_trace()
        self.dfs(nums, 0, [])
        print "Final:", self.result
        return self.result


    def dfs(self, nums, index, res):

        if index == len(nums):
            self.result.append(copy.deepcopy(res))
            print "res:", res
            return

        for i in nums:
            if not self.isTaken[i]:
                res.append(i)
                self.isTaken[i] = True
                self.dfs(nums, index+1, res)
                self.isTaken[i] = False
                res.pop()

a = Solution()
print a.permute([1,2,3])
