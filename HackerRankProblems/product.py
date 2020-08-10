class Solution(object):
	def productExceptSelf(self, nums):
		result = [None]*len(nums)
		self.product(nums, result, 0, 1, 1)
		print result
		return result

	def product(self, nums, result, index, before, after):

		if index > len(nums) - 1:
			return 1
		res = self.product(nums, result, index+1, before*nums[index], after)
		pro = before * res
		result[index] = pro
		return res*nums[index]


a = Solution()
a.productExceptSelf([1,2,3,4])
