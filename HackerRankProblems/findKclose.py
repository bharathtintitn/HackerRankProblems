import pdb

class Solution(object):

    def findClosestElements(self, arr, k, x):
        print "*********************"
        index = self.binarySearch(0, len(arr)-1, arr, x)
        print "index:", index
        i, j = index-1, index + 1
        count = 1
        result = [arr[index]]
        while count < k:
            if i >= 0 :
                if (j < len(arr)):
                    if (abs(x-(arr[i])) <= abs(x-(arr[j]))):
                        result.append(arr[i])
                        i -= 1
                        count += 1
                else:
                    result.append(arr[i])
                    i -= 1
                    count += 1
            if j <= len(arr)-1 and count < k and (abs(x-(arr[j])) < abs(x-(arr[i]))):
                result.append(arr[j])
                j += 1
                count += 1

        #print result
        result = sorted(result)
        return result

    def binarySearch(self, start, end, arr, target):

        if start < end:
            mid = (start+end)/2
            print "mid:", mid

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return self.binarySearch(start, mid-1, arr, target)
            else:
                return self.binarySearch(mid+1, end, arr, target)
        return start

a = Solution()
print a.findClosestElements([1,2,3,4,5], 4, 3)
print a.findClosestElements([1,2,3,4,5], 4, -1)
print a.findClosestElements([1,2,3,4,5], 4, 6)
print a.findClosestElements([0,0,0,1,3,5,6,7,8,8], 2, 2)
print a.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4)
