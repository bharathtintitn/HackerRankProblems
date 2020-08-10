class Solution(object):

	def binarySearch(self, start, end, n, target):

		if start < end:
			mid = (start+end)/2
			print "mid:", mid
			if n[mid] == target:
				return mid
			elif n[mid] > target:
				return self.binarySearch(start, mid-1, n, target)
			else:
				return self.binarySearch(mid+1, end, n, target)
		return start

	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		if len(nums) == 0:
			return result
		elif len(nums) == 1:
			return [0]
		else:
			n = sorted(nums)
			print "n:", n
			print "nums:", nums
			for find in nums:
				index = self.binarySearch(0, len(nums)-1, n, find)
				add = len(nums) - index
				print "index:", index, " add:", add
				result.append(index)
			print "Result:", result
		return result

a = Solution()
print a.countSmaller([5,2,6,1])
