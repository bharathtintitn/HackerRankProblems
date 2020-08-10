import pdb

class Solution(object):

    def restoreString(self, s, indi):

        index = 0
        print "*********"
        if len(s) < 1:
            return s
        s = list(s)
        while index < len(s):
            #pdb.set_trace()
            if index == indi[index]:
                index += 1
            else:
                s[index], s[indi[index]] = s[indi[index]], s[index]
                temp = indi[index]
                indi[index] = indi[indi[index]]
                indi[temp] = temp
                #indi[indi[index]] = temp
                #indi[index], indi[indi[index]] = indi[indi[index]], indi[index]

            print "s:{}, indi:{}, index:{}".format(s, indi, index)

        print s
        return "".join(s)

a = Solution()
print a.restoreString("codeleet", [4,5,6,7,0,2,1,3])
print a.restoreString("abc", [0,1,2])
print a.restoreString("aiohn", [3,1,4,2,0])
