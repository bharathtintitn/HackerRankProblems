import pdb
from collections import defaultdict

class Solution(object):

    def groupStrings(self, strings):

        def separate(array):
            result = defaultdict(list)
            if len(array) == 0:
                return result
            if len(array) == 1:
                return array
            index = 1
            for string in strings:
                res = []
                for i in xrange(len(string)-1):
                    res.append((ord(string[i]) - ord(string[i+1]))%26)
                result[tuple(res)].append(string)
            print result.values()
            return result.values()


        return separate(strings)

a = Solution()
a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
