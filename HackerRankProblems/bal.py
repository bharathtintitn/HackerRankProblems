from collections import Counter
class Solution(object):

    def balancedString(self, s):
        length = len(s)
        print "length:",length

        if length < 4:
            return 0
        expect = length//4
        print "expected:",expect
        freq = Counter(s)
        print freq
        replace = 0
        for i,j in freq.iteritems():
            if j > expect:
                replace = replace + (j - expect)

        print "replace:", replace
        print "============="
        return replace


a = Solution()
print a.balancedString("QQQQ")
print a.balancedString("QWER")
print a.balancedString("QQWE")
print a.balancedString("QQQW")
print a.balancedString("WWEQERQWQWWRWWERQWEQ")
