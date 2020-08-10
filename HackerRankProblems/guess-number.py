

class Solution(object):
    def search(self, nums, target):

        return self.bsearch(nums, 0, len(nums)-1, target)

    def search1(self, nums, start, end, target):
        if start <= end:
            mid = (start + end)/2
            print "mid:", mid
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target <= nums[end]:
                return self.bsearch(nums, mid+1, end, target)
            else:
                return self.bsearch(nums, start, mid-1, target)
        return -1

    def bsearch(self, nums, start, end, target):

        if start <= end:

            mid = (start+end)/2
            print "Mid:", mid
            if nums[mid] == target:
                return mid
            elif nums[start] >= nums[mid]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1
                    return self.bsearch(nums, start, end, target)
                else:
                    return self.bsearch(nums, start, mid-1, target)
            else:
                if target < nums[mid] and target >= nums[start]:
                    return self.bsearch(nums, start, mid-1, target)
                return self.bsearch(nums, mid+1, end, target)
        return -1


a = Solution()
print a.search([4,5,6,7,0,1,2], 3)
print a.search([4,5,6,7,0,1,2], 0)
