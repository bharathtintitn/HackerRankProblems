import pdb

class Solution(object):

    def trap(self, heights):

        n = len(heights)

        if n == 0:
            return 0

        left = []
        so_far = -1
        for num in heights:
            so_far = max(num, so_far)
            left.append(so_far)

        print left
        right = []
        so_far = -1
        for num in reversed(heights):
            so_far = max(num, so_far)
            right.append(so_far)
        right = [i for i in reversed(right)]
        print right
        total = 0
        print heights
        for i in xrange(n):
            total += (min(left[i], right[i]) - heights[i])

        print total

a = Solution()
a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
