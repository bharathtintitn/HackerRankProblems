import pdb

class Solution(object):

    def search(self, nums, target):

        index = self.binarySearch(0, len(nums)-1, nums, target)
        print "final:", index
        return True if nums[index] == target else False


    def binarySearch(self, start, end, nums, target):

        if start <= end:
            mid = (start+end)/2
            print "mid:", mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target and nums[mid] > nums[start]:
                return self.binarySearch(start, mid-1, nums, target)
            elif nums[mid] > target and nums[mid] < nums[start]:
                return self.binarySearch(mid+1, end, nums, target)
            elif nums[mid] < target and nums[mid] < nums[start]:
                return self.binarySearch(start, mid-1, nums, target)
            elif nums[mid] < target and nums[mid] > nums[start]:
                return self.binarySearch(mid+1, end, nums, target)
        return start

a = Solution()
print a.search([2,5,6,0,0,1,2], 0)
print a.search([2,5,6,0,0,1,2], 3)
