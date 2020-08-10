class Solution(object):
    def isIsomorphic(self, s, t):
		print "***************"
		if s == t:
			return True
		convert = {}
		taken = set()
		for i, j in enumerate(s):
			if convert.get(j, False):
				if convert[j] <> t[i]:
					return False
			else:
				if t[i] not in taken:
					convert[j] = t[i]
				else:
					return False
				taken.add(t[i])
		print "covert:", convert
		print "taken:", taken
		#if len(convert) <> len(t):
		#	return False
		return True


a = Solution()
print a.isIsomorphic("egg", "add")
print a.isIsomorphic("foo", "bar")
print a.isIsomorphic("paper", "title")
print a.isIsomorphic("ab", "aa")
