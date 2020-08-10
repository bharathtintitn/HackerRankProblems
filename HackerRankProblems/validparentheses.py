import pdb

class Solution(object):

    def isValid(self, s):

        print "************"
        if len(s) == 0:
            return True

        stack = []
        #d = {'(': ')', "{": "}", "[": "]"}
        d = {')': '(', "}": "{", "]": "["}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if stack:
                    item = stack.pop()
                    print "Item:", item, ' d:', d[i]
                    if d.get(i, False) and d[i] == item:
                        continue
                    else:
                        return False
                else:
                    return False
            print "Stack:", stack, " i:", i

        return True if len(stack) == 0 else False

a = Solution()
print a.isValid("()"), " True"
print a.isValid("(]"), ' False'
print a.isValid("()[]{}"), ' True'
print a.isValid("([)]"), ' False'
print a.isValid("([)]"), ' False'
print a.isValid("{[]}"), ' True'
print a.isValid("]"), ' False'
