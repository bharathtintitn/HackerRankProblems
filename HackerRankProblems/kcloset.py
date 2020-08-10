import pdb

class Solution(object):

    def findClosestElements(self, arr, k, x):

        index = self.binarySearch(arr, 0, len(arr)-1, x)
        print "index:", index
        result = []
        i = index
        up = False
        pdb.set_trace()

        #i, j = index, index + 1
        j = index - k
        print "j:", j
        while k > 0:
            if j < 0:
                result.append(arr[index])
                index += 1
            else:
                result.append(arr[j])
                j += 1
            k -= 1
        print "result:", result
        return result

    def binarySearch(self, arr, start, end, target):
        #pdb.set_trace()
        if start < end:
            mid = (start+end)/2
            print "Mid:", mid
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return self.binarySearch(arr, start, mid-1, target)
            else:
                return self.binarySearch(arr, mid+1, end, target)
        return start

a = Solution()
print a.findClosestElements([1,2,3,4,5], 4, 3)
print a.findClosestElements([1,2,3,4,5], 4, -1)
