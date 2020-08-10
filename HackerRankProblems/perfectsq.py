import pdb
from collections import deque

class Solution(object):

    def numSquare(self, n):
        print "******"
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        i = 2
        square = deque([1])
        while i < n+1:
            print "i:{}, dp:{}".format(i, dp)
            #pdb.set_trace()
            for s in square:
                    if i < s:
                        break
                    dp[i] = min(dp[i-1]+1, dp[i-s]+1, dp[i])
            add = (i*i)
            square.append(add)
            i += 1

        print "Final:",dp
        return dp[n]


a = Solution()
print a.numSquare(12)
print a.numSquare(13)
