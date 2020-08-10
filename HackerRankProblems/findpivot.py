import pdb
class Solution(object):
    def pivotIndex1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        end = len(nums)
        leftsum = 0
        rightsum = 0
        mid = 0 + (end - 0)/2
        print "Mid:", mid
        
        for i in xrange(mid):
            leftsum += nums[i]
            
        print "Leftsum:", leftsum
        
        for i in xrange(mid+1, len(nums)):
            rightsum += nums[i]
        
        print "Rightsum:", rightsum
        
        if leftsum == rightsum and len(nums) > 0:
            return mid
        elif len(nums) == 0:
            return -1
        else:
			right = False
			left = False
			i = mid
			j = mid
			if rightsum > leftsum:
				right = True
			if leftsum > rightsum:
				left = True
			pdb.set_trace()
			print "Right:", right, " left:", left, " mid:", mid
			while (mid >= 0 and mid <= len(nums)-1):
				print "Rightsum:", rightsum, " leftsum:", leftsum
				if not right and not left:
					break
				
				if right:
					ritem = nums[mid]
					litem = nums[mid-1]
					mid -= 1
					print "Adding:", ritem, " ", rightsum + ritem
					rightsum += ritem
					print "sub:", litem, " ", leftsum + litem
					leftsum -= litem
					if rightsum == leftsum:
						return mid
					
				if left:
					litem = nums[mid]
					ritem = nums[mid+1]
					mid += 1
					print "Adding:", ritem, " ", rightsum + ritem
					rightsum += ritem
					print "sub:", litem, " ", leftsum + litem
					leftsum -= litem
					if rightsum == leftsum:
						return mid
			return -1

    def pivotIndex(self, nums):
		
		from collections import OrderedDict
		if not nums: return -1

		summap = OrderedDict()
		summap[-1] = 0
		acc = 0
		ans = []

		for i, n in enumerate(nums):
			acc += n
			summap[i] = acc
		end = len(nums) - 1
		total = summap[end]
		res = []
		print "Total:", total
		print "summap:", summap
		print "nums:", nums
		for i in reversed(xrange(len(nums))):
			print "i:", i, " diff:", total-summap[i], ' sum:', summap[i-1]
			if total - summap[i] == summap[i-1]:
				res.append(i)
		print "Res:", res
		if res:
			return min(res)
		return -1
a = Solution()
print a.pivotIndex([-1,-1,-1,-1,-1,0])
