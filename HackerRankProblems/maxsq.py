import pdb
class Solution(object):
    def maximalSquare(self, matrix):
		ilength = len(matrix)
		if ilength == 0:
			return 0

		jlength = len(matrix[0])
		dp = [[0]*jlength for i in xrange(ilength)]
		print "DP:", dp
		maxs = 0
		for i in xrange(0, ilength):
			for j in xrange(0, jlength):
				if i == 0 or j == 0:
					dp[i][j] = int(matrix[i][j])
				else:
					#pdb.set_trace()
					if matrix[i][j] == '1':
						#pdb.set_trace()
						#dp[i][j] = min(int(matrix[i][j]), int(matrix[i-1][j]), int(matrix[i-1][j-1])) + 1
						dp[i][j] = min(int(dp[i][j-1]), int(dp[i-1][j]), int(dp[i-1][j-1])) + 1

				if dp[i][j] > maxs:
					maxs = dp[i][j]
		print "mat:", matrix
		print "dp:", dp
		print "maxs:", maxs
		return maxs*maxs
a = Solution()
a.maximalSquare([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]) 
