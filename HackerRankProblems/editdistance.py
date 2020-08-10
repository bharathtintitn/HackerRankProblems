import pdb

class Solution(object):

    def minDistance(self, word1, word2):

        dp = [[None for j in xrange(len(word2)+1)] for i in xrange(len(word1)+1)]
        print "dp:", dp
        for i in xrange(len(word1)+1):
            for j in xrange(len(word2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                        #dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        print "dp:", dp
        return dp[len(word1)][len(word2)]

a = Solution()
print a.minDistance("horse", 'ros')
print a.minDistance('intention', 'execution')
print a.minDistance("zoologicoarchaeologist", "zoogeologist")
