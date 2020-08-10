class Solution(object):
    def binary_search(self, start, end, target, nums, found, find_start, find_end, pos_start, pos_end):

        if start <= end:
            mid = start + (end - start)/2
            print "Mid:", mid
            if found:
                if nums[mid] != target:
                    return pos_start, pos_end
                if find_start:
                    pos_start, pos_end = self.binary_search(start, mid-1, target, nums, found, find_start, find_end, mid, pos_end)
                    return pos_start, pos_end
                if find_end:
                    pos_start, pos_end = self.binary_search(mid+1, end, target, nums, found, find_start, find_end, pos_start, mid)
                    return pos_start, pos_end
            if nums[mid] == target:
                found = True
                pos_start, _ = self.binary_search(start, mid-1, target, nums, found, True, False,  mid, mid)
                _, pos_end = self.binary_search(mid+1, end, target, nums, found, False, True, pos_start, mid)
                return pos_start, pos_end

            elif nums[mid] < target:
                a, b = self.binary_search(mid+1, end, target, nums, found, find_start, find_end, pos_start, pos_end)

            else:
                a, b = self.binary_search(start, mid-1, target, nums, found, find_start, find_end, pos_start, pos_end)
            return a, b
        if found:
            return  pos_start, pos_end 
        return -1, -1

    def binarySearch(self, start, end, nums, target):

        if start <= end:
            mid = start + (end-start)/2
            print "mid:", mid
            if nums[mid] == target:
                a, b = self.binarySearch(start, mid-1, nums, target)
                y, z = self.binarySearch(mid+1, end, nums, target)
                start = mid
                end = mid
                if a < start and a != -1:
                    start = a
                if y < start and y != -1:
                    start = y
                if b > end and b != -1:
                    end = b
                if z > end and z != -1:
                    end = z
                return start, end
            elif nums[mid] > target:
                return self.binarySearch(start, mid-1, nums, target)
            else:
                return self.binarySearch(mid+1, end, nums, target)

        return -1, -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import pdb
        pdb.set_trace()
        #a, b = self.binary_search(0, len(nums)-1, target, nums, False, False, False,  -1, -1)
        a, b = self.binarySearch(0, len(nums)-1, nums, target)
        print a, b
        return a, b


a = Solution()
a.searchRange([5,7,7,8,8,10], 8)
a.searchRange([5,7,7,8,8,10], 6)
a.searchRange([2, 2], 2)
a.searchRange([1,2,3,3,3,3,4,5,9], 3)
