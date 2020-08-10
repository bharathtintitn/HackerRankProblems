import pdb

class Solution(object):

    def numDecodings(self, s):

        self.dp = {}
        self.recurr(0, s)
        print self.dp

    def recurr(self, index, s):

        if index > len(s) - 1:
            return 1

        if index < len(s) and s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        if self.dp.get(index, False):
            return self.dp[index]

        one = self.recurr(index + 1, s)
        print "==>{}, {} {}".format(s[index], s[index:index+2], one)
        if int(s[index:index+2]) <= 26:
            one += self.recurr(index+2, s)
            print "two:", one
        self.dp[index] = one
        return one

a = Solution()
pdb.set_trace()
a.numDecodings("2326")
