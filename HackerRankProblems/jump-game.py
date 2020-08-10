import pdb
class Solution(object):
	def canJump(self, nums):
		return self.go_recur(nums, 0)

	def go_recur(self, nums, index):

		if index == len(nums) - 1:
			return True
                if index >= len(nums):
                        return False
		#pdb.set_trace()
		temp = nums[index]
		while temp > 0:
			if not self.go_recur(nums, index+temp):
				temp -= 1
			else:
				return True
		return False



a = Solution()
#print a.canJump([2,3,1,1,4])
#print a.canJump([3,2,1,0,4])
print a.canJump([2,0])
