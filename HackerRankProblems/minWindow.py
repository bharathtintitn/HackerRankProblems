import pdb
from collections import Counter, defaultdict

class Solution(object):

    def minWindow(self, s, t):

        lengtht = len(t)
        lengths = len(s)
        if lengtht == 0 or lengths == 0:
            return ""

        dicts = Counter(s)
        dictt = Counter(t)
        found = defaultdict(int)

        formed = 0
        i, j = 0,0
        ans, lo, hi = None, 0, lengths
        #pdb.set_trace()
        while j < lengths:

            character = s[j]
            found[character] += 1
            if dictt[character] > 0 and found[character] == dictt[character]:
                formed += 1
            while i <= j and formed == lengtht:
                ch = s[i]

                if (j - i + 1) < (hi - lo) and formed == lengtht:
                    ans, lo, hi = s[i:j+1], i, j
                if found[ch] >= dictt[ch] and formed == lengtht:
                    found[ch] -= 1
                    if found[ch] < dictt[ch]:
                        formed -= 1
                i += 1
            j += 1

        print ans, lo, hi
        return ans

a = Solution()
print a.minWindow("ADOBECODEBANC", "ABC")
