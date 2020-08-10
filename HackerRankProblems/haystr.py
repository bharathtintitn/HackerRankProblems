class Solution(object):
    def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""

		return haystack.find(needle)

a = Solution()
print a.strStr("hello", "ll")
print a.strStr("aaaaa", "bba")
