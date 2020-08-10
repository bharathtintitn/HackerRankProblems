import pdb
from collections import defaultdict

class Solution(object):

    def countSubstrings(self, s):
        pdb.set_trace()
        self.string = defaultdict(bool)
        #self.ispali(s, 0, len(s)-1)
        self.pali(s, 0, len(s)-1)
        print self.string
        return [] if not self.string else [i for i,j in self.string.iteritems() if j]

    def ispali(self, s, start, end):

        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        print s
        return True

    def pali(self, s, start, end):

        if start <= end:
            if self.string[s[start:end+1]]:
                return
            if self.ispali(s, start, end):
                self.string[s[start:end+1]] = True
            self.pali(s, start+1, end)
            self.pali(s, start, end-1)
            self.pali(s, start+1, end-1)


a = Solution()
print a.countSubstrings('abc')
print a.countSubstrings('aaa')
