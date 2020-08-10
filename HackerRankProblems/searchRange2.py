
class Solution(object):

    def searchRange(self, nums, target):

        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        low = self.binarySearch(0, len(nums)-1, target, nums, True)
        print "low:", low, target
        if low == -1 or nums[low] <> target:
            return [-1, -1]

        high = self.binarySearch(0, len(nums)-1, target, nums, False)
        import pdb
        pdb.set_trace()
        if high > 0 and high == target:
            return [low, high]
        print "low:", low, " high:", high
        return [low, high-1]

    def binarySearch(self, start, end, target, nums, left):

        if start < end:

            mid = (start+end)/2
            print "mid:", mid
            if nums[mid] == target and left:
                return self.binarySearch(start, mid, target, nums, left)
            elif nums[mid] > target:
                return self.binarySearch(start, mid, target, nums, left)
            else:
                return self.binarySearch(mid+1, end, target, nums, left)

        return start

a = Solution()
print a.searchRange([5,7,7,8,8,10], 8)
print a.searchRange([5,7,7,8,8,10], 6)
print a.searchRange([2,2], 2)
