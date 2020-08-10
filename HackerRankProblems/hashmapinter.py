import pdb
from collections import defaultdict
class Solution:
    def intersect(self, nums1, nums2):
	freq = defaultdict(int)
	for i in nums1:
		freq[i] += 1
	print(freq)
	result = []
	for i in nums2:
		if freq[i] > 0:
			result.append(i)
			freq[i] -= 1
	print result

a = Solution()
print a.intersect([1,2,2,1], [2,2])
print a.intersect([4,9,5], [9,4,9,8,4])
   
