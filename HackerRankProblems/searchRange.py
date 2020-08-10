class Solution(object):
	def searchRange(self, nums, target):
		import pdb
		#pdb.set_trace()

		if len(nums) == 0:
			return [-1, -1]
		if len(nums) == 1:

			if target == nums[0]:
				return [0, 0]
			else:
				return [-1, -1]

		if len(nums) == 2:
			if nums[0] == nums[1]:
				return [0, 1]
			if target == nums[0]:
				return [0, 0]

			if target == nums[1]:
				return [1, 1]
			return [-1, -1]

		ret = self.binarySearch(0, len(nums)-1, target, nums)
		if ret == -1:
			return [-1, -1]
		else:
			if type(ret[0]) == list :
			 	l = ret[0][0]
			else:
				l = ret[0]
			if type(ret[1]) == list :
				r = ret[1][0]
			else:
				r = ret[1]
			return [l, r]

	def binarySearch(self, start, end, target, nums):

		if start+1 < end:
			mid = (start+end)/2
			print "mid:", mid
			if nums[mid] == target:
				s = self.binarySearch(start, mid, target, nums)
				start = mid if s == -1 else s
				e = self.binarySearch(mid, end, target, nums)
				end = mid if e == -1 else e
				return [start, end]
			elif nums[mid] > target:
				return self.binarySearch(start, mid, target, nums)

			else:
				return self.binarySearch(mid, end, target, nums)

		return -1


a = Solution()
print a.searchRange([5,7,7,8,8,10], 8)
print a.searchRange([5,7,7,8,8,10], 6)
