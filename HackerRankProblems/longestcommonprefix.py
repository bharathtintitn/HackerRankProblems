import pdb

class Solution(object):

    def longestCommonPrefix(self, strings):
        print "**************"
        result = ""
        length = len(strings)
        if length == 0:
            return ""

        verify = strings[0]
        print "verifier:", verify

        freq = {}
        for c in verify:
            #if freq.get(c, False):
            freq[c] = 1
            #else:
            #    freq[c] = 1
        print 'Freq:', freq

        for i in xrange(1, length):
            string = strings[i]
            for c in string:
                if freq.get(c, False):
                    freq[c] += 1
                else:
                    break

        print "freq:", freq

        pdb.set_trace()
        for c in verify:
            if freq.get(c, False):
                if freq[c] <> 0 and freq[c]%length == 0:
                    result += c
                else:
                    break
            else:
                break
        print "result:", result
        return result

a = Solution()
print a.longestCommonPrefix(["flower","flow","flight"])
print a.longestCommonPrefix(["dog","racecar","car"])
print a.longestCommonPrefix(["aa","ab"])
