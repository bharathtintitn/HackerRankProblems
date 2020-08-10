class Solution(object):
	def checkStraightLine(self, coordinates):
		diffx, diffy = 0,0
		prevx, prevy = 0,0
		for i in xrange(len(coordinates)-1):
			a = coordinates[i]
			b = coordinates[i+1]
			
			diffx = abs(a[0] - b[0])
			print "diff x:", diffx
			diffy = abs(a[1] - b[1])
			print "diff y:", diffy
			if not prevx and not prevy:
				prevx = diffx
				prevy = diffy
			if prevx <> diffx or prevy <> diffy:
				return False
		return True

a = Solution()
print a.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
print a.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
print a.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]])
