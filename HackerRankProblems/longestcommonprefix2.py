import pdb

class Solution(object):

    def validate(self, strings, index, i, c,  result):

        if index > len(strings) - 1:
            return True
        string = strings[index]
        if i > (len(string)-1):
            return False
        if string[i] == c and self.validate(strings, index+1, i, c, result):
            return True
        return False

    def longestCommonPrefix(self, strings):
        length = len(strings)
        if length == 0:
            return ""
        if length == 1:
            return strings[0]
        result = ''
        for i in xrange(len(strings[0])):
            c = strings[0][i]
            print "character:", c
            if self.validate(strings, 1, i, c, result):
                result += c
            else:
                print "final:", result
                return result


a = Solution()
print a.longestCommonPrefix(["flower","flow","flight"])
print a.longestCommonPrefix(["dog","racecar","car"])
print a.longestCommonPrefix(["aa","ab"])
