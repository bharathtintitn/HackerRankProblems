import pdb

class Solution(object):

    def maximalRectangle(self, matrix):

		def getMax(height):

			stack = [-1]
			area = 0
			for i in xrange(len(height)):
				while stack[-1] <> -1 and height[stack[-1]] >= height[i]:
					area = max(area, height[stack.pop()] * (i - 1 -stack[-1]))
				stack.append(i)

			while stack[-1] <> -1:
				area = max(area, height[stack.pop()] * (len(height) -1- stack[-1]))
			return area

		if not matrix:
			return 0
		y = len(matrix)
		x = len(matrix[0])
		dp = [[0]*x for i in xrange(y+1)]
		print dp
		pdb.set_trace()
		for i in xrange(y):
			for j in xrange(x):
				if j == 0:
					dp[i+1][j] = 0 if matrix[i][j] == '0' else dp[i][j] + 1
				else:
					if matrix[i][j] <> '0':
						dp[i+1][j] = 1 + dp[i][j]
					else:
						dp[i+1][j] = 0

		print "final:", dp
		max_value = 0
		for i in xrange(1, y+1):
			value = getMax(dp[i])
			max_value = max(value, max_value)
		print "max_value:", max_value
		return max_value

a = Solution()
a.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])
