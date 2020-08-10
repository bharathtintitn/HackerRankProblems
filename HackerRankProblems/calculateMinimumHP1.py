import pdb

class Node(object):

    def __init__(self):
        self.health = 0
        self.minHealth = float('inf')

class Solution(object):

    def calculateMinimumHP(self, dun):

        m = len(dun)
        if m == 0:
            return 1
        n = len(dun[0])

        dp = [[Node()]*(n+1) for i in xrange(m+1)]
        print "dp:", dp

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if dun[i][j] >= 0:
                    if dp[i][j-1].minHealth <  dp[i-1][j].minHealth:
                        copy = dp[i][j-1]
                    else:
                        copy = dp[i-1][j]
                    dp[i][j].minHealth = copy.minHealth
                    dp[i][j].health = copy.health + dun[i][j]

a = Solution()
assert a.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]), 7
