'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
import pdb
from typing import List


class Solution(object):

    def maxSubArray(self, nums: List[int]) -> int:
        pdb.set_trace()
        result = self.split_array(0, len(nums)-1, nums)
        print('Final:', result)
        return result

    def cross_over(self, start, end, mid, nums):

        if start == end:
            return nums[start]

        leftsum = float('-inf')
        curr_sum = 0
        for i in range(mid, start-1, -1):
            curr_sum += nums[i]
            leftsum = max(curr_sum, leftsum)

        rightsum = float('-inf')
        curr_sum = 0
        for i in range(mid+1, end+1):
            curr_sum += nums[i]
            rightsum = max(curr_sum, rightsum)

        return leftsum + rightsum

    def split_array(self, start: int, end: int, nums: List[int]) -> int:

        if start >= end:
            return nums[start]
        mid = (start+end)//2
        print('mid:{}'.format(mid))

        left = self.split_array(start, mid, nums)
        right = self.split_array(mid+1, end, nums)
        cross = self.cross_over(start, end, mid, nums)
        return max(left, right, cross)

a = Solution()
assert a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6


