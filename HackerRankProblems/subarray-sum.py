class Solution(object):
    def recu(self, num, i, k, total, count):
        
        if i < len(num):
            total += num[i]
	    diff = total - k
	    count += self.res_dict.get(diff, 0)
            #if total == k:
            #    count += 1
                
            i += 1
	    if self.res_dict.get(total, False):
		self.res_dict[total] += 1
	    else:
		self.res_dict[total] = 1
            count = self.recu(num, i, k, total, count)
            return count
        
        return count
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
	self.res_dict = {}
       	self.res_dict[0] = 1 
        result = 0
	total = 0
	res = self.recu(nums, 0, k, total, 0)
	result += res
	
        print result
        return result

a =Solution()
a.subarraySum([1,1,1], 2)
import pdb
pdb.set_trace()
a.subarraySum([1,2,3], 3)
