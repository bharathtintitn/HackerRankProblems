import pdb

class Solution(object):

    def Knapsack(self):

        weight = [5, 3, 4, 2]
        item = [70, 50, 60, 40]

        dp = [[0 for i in xrange(6)] for j in xrange(5)]
        print dp
        pdb.set_trace()
        for i in xrange(1,5):
            for j in xrange(1, 6):
                print "i,j:", i, j, dp[i-1]
                if weight[i-1] <= j:
                    print "i,j:", i, j, dp[i-1]
                    print j-weight[i-1]
                    if j - weight[i-1] >= 0:
                        index = j-weight[i-1]
                        value = max(item[i-1], item[i-1]+dp[i-1][index], dp[i-1][j])
                    else:
                        value = max(item[i-1], dp[i-1][j])
                    dp[i][j] = value
                else:
                    dp[i][j] = dp[i-1][j]

        print dp

a = Solution()
a.Knapsack()
