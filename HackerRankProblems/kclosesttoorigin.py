import pdb

class Solution(object):

    def kClosest(self, points, k):

        result = []
        for point in points:
            x, y = point[0], point[1]
            distance = (x*x) + (y*y)
            result.append([distance, point])
        print result
        result = sorted(result)
        return [p[1] for i,p in enumerate(result) if i < k]

a = Solution()
print a.kClosest([[3,3],[5,-1],[-2,4]], 2)
print a.kClosest([[1,3],[-2,2]], 1)
