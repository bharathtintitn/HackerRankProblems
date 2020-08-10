import pdb

class Solution(object):

    def findDuplicates(self, nums):

        i = 0
        while i < len(nums):

            j = nums[i] - 1
            if nums[i] <> nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        print nums
        res = []
        for i,j in enumerate(nums):

            if i+1 == nums[i]:
                continue
            res.append(j)
        print res
        return res
a = Solution()
a.findDuplicates([4,3,2,7,8,2,3,1])
