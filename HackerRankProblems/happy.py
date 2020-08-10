

class Solution(object):
    def isHappy(self, n):
        print "########################"
        if n == 0:
            return False
        if n == 1:
            return True
        total = 0
        result = []
        while True:
            if total == 1 or total in result:
                break
            print "total:",total
            #if n < 10 or (n in result and len(result)>1):
            #    result.append(n)
            #    total += (n*n)
            #    n = total
            #    total = 0
            #else:
            while n > 0:
                    if n % 10 == 0:
                        n = n/10
                    else:
                        add = n%10
                        print "add:", add
                        total += (add*add)
                        n = n/10
                        print "Change n:", n
            else:
                    if total in result:
                        break
                    result.append(total)
                    print "result:", result
                    n = total
                    total = 0
        return  total == 1

a = Solution()
import pdb
pdb.set_trace()
print a.isHappy(10) 
print a.isHappy(19)
print a.isHappy(20)
print a.isHappy(2)


