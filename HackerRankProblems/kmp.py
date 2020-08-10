

class Solution(object):

    def repeatedSubstringPattern(self, s):

        dp = self.kmp(s)
        self.nkmp(s)
        z_count = 0
        max_count = 0
        #for i in dp:
        #    if i == 0:
        #        z_count += 1
        #    max_count = max(i, max_count)

        print z_count, max_count
        if dp[-1] * 2 < len(s):
            return False
        common = dp[-1]-len(s)
        if len(s)%common == 0:
            return True
        return False

    def nkmp(self, s):

        length = 0
        dp = [0]*len(s)
        for i in xrange(1, len(s)):
            if s[i] == s[length]:
                dp[i] = length + 1
                i += 1
                length += 1
            else:
                if length == 0:
                    i = i + 1
                else:
                    length = dp[length-1]
        print "new dp:", dp

    def kmp(self, string):

        index = 0
        dp = [0]*len(string)
        for i in xrange(1, len(string)):
            if string[i] == string[index]:
                dp[i] = dp[i-1] + 1
                index += 1
        print "dp:", dp
        return dp

a = Solution()
print a.repeatedSubstringPattern('abab')
print "#############"
print a.repeatedSubstringPattern('abcabcabcabc')
print "#############"
print a.repeatedSubstringPattern('aba')
print "#############"
import pdb
pdb.set_trace()
print a.repeatedSubstringPattern('dsgwadsgz')
