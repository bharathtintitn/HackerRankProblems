import pdb

class Solution(object):

    def largestRectangleArea(self, heights):

        return self.divided(heights, 0, len(heights)-1)

    def divide(self, heights):

        start = 1
        end = len(heights)
        #pdb.set_trace()
        if start > end:
            return float('inf'), float('-inf')
        elif start == end:
            h, a = self.conquer(heights, heights[0], heights[0])
            return h, a
        else:
            mid = (start+end)/2
            print "start:{}, end:{}, mid:{}, heights:{}, left:{}, right:{}".format(start, end, mid, heights, heights[mid:], heights[:mid])
            lh, la = self.divide(heights[mid:])
            rh, ra = self.divide(heights[:mid])
            h, a = self.conquer(heights, lh, rh)
            return h, a

    def divided(self, heights, start, end):

        if start > end:
            return 0
        min_height = start
        for i in xrange(start, end+1):
            if heights[i] < heights[min_height]:
                min_height = i
        center = heights[min_height]*(end-start+1)
        left = self.divided(heights, start, min_height-1)
        right = self.divided(heights, min_height+1, end)
        print "height:{}, start:{}, end:{}, center:{}, left:{}, right:{}, minheight:{}".format(heights, start, end, center, left, right, min_height)
        return max(center, left, right)
        #return max(min_height*(end-start+1), self.divided(heights, start, min_height-1), self.divided(heights, min_height+1, end))

    def conquer(self, heights, lh, rh):

        max_height = min(lh, rh)
        self.max_area = max(self.max_area, max_height*len(heights))

        print "max area:", self.max_area, " heights:", heights
        return max_height, self.max_area

a = Solution()
print a.largestRectangleArea([2,1,5,6,2,3])

