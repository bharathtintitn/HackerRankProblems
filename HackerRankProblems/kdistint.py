class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        freq = {}
        length = len(s)-1
        result = 0
        if length < 0:
            return 0
        if length == 0:
            if k == 0:
                return 0
            return 1
        i, j = 0, 0
        while i <= j and j < length:
            c = s[j]
            if freq.get(c, False):
                freq[c] += 1
            else:
                freq[c] = 1

            while len(freq) > k:
                d = s[i]
                freq[d] -= 1
                if freq[d] == 0:
                    del freq[d]
                i += 1

            result = max(result, j-i+1)
            j += 1
        print "result:", result
        return result

a = Solution()
a.lengthOfLongestSubstringKDistinct("eceba", 2)
a.lengthOfLongestSubstringKDistinct("aa", 1)
