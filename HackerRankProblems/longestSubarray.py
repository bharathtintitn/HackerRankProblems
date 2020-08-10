import pdb
from collections import deque, defaultdict
class Solution(object):

    def longestSubarray(self, nums, limit):
        print "************"
        max_len, i, j, diff, m, n = 0, 0, 0, 0, 0, 0
        if not nums:
            return max_len
        window = deque([nums[j]])
        m, n = nums[j], nums[j]
        winset = set()
        winset.add(nums[j])
        windict = defaultdict(int)
        windict[nums[j]] = 1
        while j < len(nums) and i <= j:
            if not m or not n:
                m, n = max(window), min(window)
            diff = abs(n - m)
            print "diff:{}, i:{}, j:{}, max:{}, m:{}, n:{}".format(diff, i, j, max_len, m, n)
            #max_len = max(max_len, j-i+1)
            if diff <= limit:
                max_len = max(max_len, j-i+1)
                j += 1
                if j < len(nums):
                    window.append(nums[j])
                    winset.add(nums[j])
                    windict[nums[j]] += 1
                    if nums[j] > m:
                        m = nums[j]

                    if nums[j] < n:
                        n = nums[j]
                else:
                    break
            else:
                i += 1
                re = window.popleft()
                windict[re] -= 1
                if windict[re] <= 0:
                    winset.remove(re)
                if re == n or re == m:
                    m, n = max(winset), min(winset)

        print max_len
        return max_len

a = Solution()
a.longestSubarray([8,2,4,7], 4)
a.longestSubarray([10,1,2,4,7,2], 5)
a.longestSubarray([4,2,2,2,4,4,2,2], 0)


