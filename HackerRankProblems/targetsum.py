import pdb

class Solution(object):

    def __init__(self):
        self.count = 0
        self.total = 0
        self.dp = {}

    def getNum(self, n):

        for i in (1, -1):
            n = n*i
            yield n

    def findTargetSumWays(self, nums, s):

        self.dfs(nums, 0, s)
        print "count:", self.count

    def dfs(self, nums, index, s):

        if index == len(nums) and self.total == s:
            self.count += 1
            return
        elif index == len(nums):
            return

        if self.dp.get((index, self.total), False):
            return self.dp[(index, self.total)]

        for i in (1, -1):
            num = (nums[index]*i)
            self.total += num
            self.dfs(nums, index+1, s)
            self.total -= num


a = Solution()
a.findTargetSumWays([1, 1, 1, 1, 1], 3)
a.findTargetSumWays([25,33,27,23,46,16,10,27,33,2,12,2,29,44,49,40,32,46,7,50], 4)
