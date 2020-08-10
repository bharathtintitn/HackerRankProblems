import pdb

class Solution(object):

    def stackpop(self, stack):

        string = ''
        result = ''
        while True:
            s = stack.pop()
            if s == '[':
                break
            if s.isdigit():
                res = int(s) * string
                result = res + result
                string = ''
            string = s + string

    def decodeString(self, st):
        print "*************"
        stack = []
        index = 0
        final = ''
        #pdb.set_trace()
        number = ''
        while index < len(st):
            ch = st[index]
            #print "ch:",ch
            if ch <> ']':
                if ch.isdigit():
                    number = number + ch
                    print "num:", number, " ch:", ch
                else:
                    if number:
                        stack.append(number)
                        number = ''
                    stack.append(ch)
            else:
                string = ''
                print "stack:", stack
                while True:
                    s = stack.pop()
                    if s == '[':
                        break
                    string = s + string
                num = stack.pop()
                print "num:", num , " string:", string
                #string = string + final
                if num.isdigit():
                    result = int(num) * str(string)
                print "result:", result
                final =  result
                print 'final:', final
                stack.append(final)
            index += 1
        print "stack:", stack
        final = "".join(stack)
        print "ret:", final
        return final

a = Solution()
print a.decodeString("3[a]2[bc]")
print a.decodeString("3[a2[c]]")
print a.decodeString("2[abc]3[cd]ef")
print a.decodeString("100[leetcode]")
