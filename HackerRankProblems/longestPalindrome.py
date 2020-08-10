import pdb
class Solution(object):

    def longestPalindrome1(self, s):

        if len(s) < 2:
            return ''
        string1 = s
        string2 = "".join(reversed(s))
        print "2:", string2

        index = 0
        length = len(s)
        print "Length:", length
        temp = ''
        max_string = ''
        for i in xrange(length):
            if string1[i] == string2[i]:
                #print "Temp:", temp
                temp += string1[i]
                continue
            else:
                if len(temp) > len(max_string):
                    max_string = temp
                temp = ''
        print "max string:", max_string
        return max_string

    def longestPalindrome(self, s):

        start = 0
        end = len(s) - 1
        length = 0
        max_length = 0

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        for i in xrange(len(s)):

            odd, oend, ostart = self.palindrome(s, i, i)
            if i < len(s) - 1:
                even, eend, estart = self.palindrome(s, i, i+1)

            length = max(odd, even, length)
            if length > (end - start):
                start = i - (length-1)/2
                end = i + length/2

        print s[start:end+1]
        print "Length:", max_length, " start:", start, " end:", end, " string:", s[start:end], " original:", s
        return s[start:end+1]

    def palindrome(self, s, start, end):

        length = 0
        while (s[start] == s[end]) and (end < len(s)) and (start >= 0):
            length = end - start + 1
            if start == 0 or end == len(s)-1:
                break
            start -= 1
            end += 1

        return end-start-1, end , start

a = Solution()
pdb.set_trace()
a.longestPalindrome('babad')
a.longestPalindrome('cbbd')
a.longestPalindrome('bb')
a.longestPalindrome('abb')

