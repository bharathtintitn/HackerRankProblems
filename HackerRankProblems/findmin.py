import pdb
class Solution(object):
    def findMin(self, nums):
        print "***********"
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        return self.binarySearch(0, len(nums)-1, nums)

    def binarySearch(self, start, end, nums):

        if start < end:
            mid = (start+end)/2
            print "Mid:", mid
            if nums[mid] < nums[start] and nums[mid] < nums[end]:
                return self.binarySearch(start, mid, nums)
            elif nums[mid] > nums[end] and nums[mid] > nums[start]:
                return self.binarySearch(mid+1, end, nums)
            else:
                if nums[mid] > nums[end]:
                    return self.binarySearch(mid+1, end, nums)
                return self.binarySearch(start, mid, nums)
        return nums[start]

a = Solution()
print a.findMin([0,1,2,4,5,6,7])
print a.findMin([4,5,6,7,0,1,2])
print a.findMin([])
print a.findMin([1])
print a.findMin([1,0])

