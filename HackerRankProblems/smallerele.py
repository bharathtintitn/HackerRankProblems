import pdb

class Solution(object):

    def countSmaller(self, nums):
        result = []
        sort = []
        for i in reversed(nums):
            result, sort = self.binarySearch(result, sort, i)

        return reversed(sort)

    def binarySearch(self, result, sort, num):

        low = 0
        hi = len(result) - 1

        while low < hi:

            mid = (low+hi)/2
            print "mid:", mid
            if result[mid] < num:
                low = mid+1
            else:
                hi = mid

        print "Low:", low, " res:", result
        #pdb.set_trace()
        #res = result[:low] + [num] + result[low:]
        if low == 0 and len(result) > 0:
            if result[0] < num:
                low = 1
        else:
            if len(result) > 0 and low == len(result)-1:
                if result[low] < num:
                   low += 1
        result.append(num)
        res = sorted(result)
        print "mod:", res
        sort.append(low)
        print "sort:", sort
        return res, sort

a = Solution()
a.countSmaller([5,2,6,1])
a.countSmaller([2,0,1])

