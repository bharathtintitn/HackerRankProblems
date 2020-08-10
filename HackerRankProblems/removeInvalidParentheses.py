import pdb
from collections import defaultdict

class Solution(object):

    def removeInvalidParentheses(self, s):

        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1

            elif i == ')':

                right = right if left > 0 else right + 1
                left = left-1 if left > 0 else left

        print left, right
        self.valid = {}
        self.recur(s, 0, 0, 0, left, right, [])
        print self.valid.keys()
        return self.valid.keys()


    def recur(self, s, index, left, right, leftr, rightr, exp):

        if index == len(s) and leftr == rightr:
            #print exp
            expre = "".join(exp)
            print expre
            self.valid[expre] = 1
        else:
            if index > len(s) - 1:
                return
            ch = s[index]
            if (ch == '(' and leftr > 0) or (ch == ')' and  rightr > 0):
                self.recur(s, index+1, left, right, leftr - (1 if ch == '(' else 0), right - (1 if ch == ')' else 0), exp)
            exp.append(ch)
            if ch not in ['(', ')']:
                self.recur(s, index+1, left, right, leftr, rightr, exp)
            elif ch == '(':
                    self.recur(s, index+1, left+1, right, leftr, rightr, exp)
            elif ch == ')' and right < left:
                    self.recur(s, index+1, left, right+1, leftr, rightr, exp)
            exp.pop()


a = Solution()
#pdb.set_trace()
a.removeInvalidParentheses("()())()")
#pdb.set_trace()
a.removeInvalidParentheses("(a)())()")
#pdb.set_trace()
a.removeInvalidParentheses(")(")
