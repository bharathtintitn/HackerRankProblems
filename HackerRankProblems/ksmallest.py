import pdb

class Solution(object):

    def kthSmallest(self, matrix, k):

		if len(matrix) == 0:
			return 0

		n = len(matrix)
		m = len(matrix[0])
		print "n:", n, " m:", m

		row = k/n
		print "row:", row
		index = k%n
		print "index:", index
		if k%n == 0:
			row -= 1

		if index == 0:
			index = n - 1
		else:
			index = index - 1
		print "final index:", index

		one =  matrix[row][index]
		two =  matrix[index][row]
		print "one:", one
		print "two:", two

		if one > two:
			return two
		return one

a = Solution()
#print a.kthSmallest([
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
#], 2)
print a.kthSmallest([[1,2],[1,3]], 3)
