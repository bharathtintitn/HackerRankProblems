class Solution(object):
    def findPeakElement(self, nums):

        if len(nums) <= 2:
            if len(nums) == 2:
                return 0 if nums[0] > nums[1] else 1
            if len(nums) == 1:
                return 0
            return -1
        mid = self.binarySearch(0, len(nums), nums)
        if mid == 0:
                i = float('-inf')
        else:
                i = nums[mid-1]
        if mid == len(nums)-1:
                j = float('-inf')
        else:
                j = nums[mid+1]
        print "r mid:", nums[mid], " i:", i, " j:", j
        if (nums[mid] > i and nums[mid] > j) or (nums[mid] > j and nums[mid] > i):
            return mid
        return -1
    def binarySearch(self, start, end, nums):

        if start < end:
            mid = (start+end)/2
            print "mid:", mid
            if mid == 0:
                i = float('-inf')
            else:
                i = nums[mid-1]
            if mid == len(nums)-1:
                j = float('-inf')
            else:
                j = nums[mid+1]
            print "mid:", nums[mid], " i:", i, " j:", j
            if (nums[mid] > i and nums[mid] > j) or (nums[mid] > j and nums[mid] > i):
                return mid
            else:
                iindex = self.binarySearch(start, mid-1, nums)
                if iindex == -1:
                    jindex = self.binarySearch(mid, end, nums)
                    return jindex
                return iindex
        return -1

a = Solution()
print a.findPeakElement([1,2,3,1])
print a.findPeakElement([1,2,1,3,5,6,4])
