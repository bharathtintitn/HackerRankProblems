class Solution(object):
    def binarySearch(self, start, end, target, nums):
        if start <= end:
            mid = start + (end-start)/2
            #print "Mid:", mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(start, mid-1, target, nums)
            else:
                return self.binarySearch(mid+1, end, target, nums)
        return -1
    def threeSum(self, nums):

        array = sorted(nums)
        print "Sorted:", array
        start = 0
        end = len(nums)-1
        result = set()
        dicti = {}
        for j, i in enumerate(nums):
            dicti[i] = j
        print dicti
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                find = array[i] + array[j]
                print "Find:", find, " first:", array[i], ' second: ', array[j]
                #index = self.binarySearch(0, end, find*-1, array)
                index = dicti.get(find, -1)
                if index != i and index !=j and index != -1:
                    if i < index:
                        if j < index:
                            result.add((array[i], array[j], array[index]),)
                        else:
                            result.add((array[i], array[index], array[j]),)
                    else:
                        result.add((array[index], array[i], array[j]))
        print "result:", result
        return [[i,j,k] for i,j,k in result]

a = Solution()
print a.threeSum([-1, 0, 1, 2, -1, -4])
