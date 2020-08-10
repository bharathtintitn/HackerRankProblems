import pdb
class Solution(object):
    
    def binary_search(self, start, end, nums):
        
        while start < end:
	    pdb.set_trace()
            mid = (start+end)/2
            print "mid:", mid, "start:", start, "end:", end
            if mid == 0:
                if nums[mid] <> nums[mid+1]:
                    return nums[mid]
                else:
                    start = mid + 2
                    continue
            if mid == len(nums) - 1:
                if nums[mid] <> nums[mid-1]:
                    return nums[mid]
                else:
                    end = mid - 2
                    continue
            if nums[mid] <> nums[mid+1] and nums[mid] <> nums[mid-1]:
                return nums[mid]
            elif nums[mid] == nums[mid+1]:
                if (mid - start - 1)%2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
            #else nums[mid] == nums[mid-1]:
            else:
                print "start:", start, "mid:", mid
		#pdb.set_trace()
                if (mid - start - 1) % 2 <> 0:
                    end = mid - 2
                #if (end + mid + 1)%2 == 0:
                #    end = mid - 2
                else:
                    start = mid + 1
                
        return nums[start]
            
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binary_search(0, len(nums)-1, nums)

a = Solution()
#print a.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print a.singleNonDuplicate([3,3,7,7,10,11,11])
