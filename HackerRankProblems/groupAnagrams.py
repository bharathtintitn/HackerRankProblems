import pdb
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
	print ans
        return ans.values()
a = Solution()
a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
a.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])

