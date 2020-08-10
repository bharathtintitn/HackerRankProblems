import pdb
class Solution(object):

    def missingNumber(self, arr):
        diff = None
        ap = None 
        result = []
        pdb.set_trace()
        for i in xrange(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            if not ap:
                print "first ap:",diff
                ap = diff
                continue
            if diff < ap:
               print "diff <:", diff
               if arr[i-1] < arr[i]:
                    return arr[i-1] + diff
               return arr[i-1] - diff
            if diff > ap:
                print "diff >:", diff
                if arr[i-1] < arr[i]:
                     return arr[i] + ap
                return arr[i] - ap

a = Solution()
print a.missingNumber([5,7,11,13])
print a.missingNumber([15,13,12])
