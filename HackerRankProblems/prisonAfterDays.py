import pdb
from collections import defaultdict

class Solution(object):

    def prisonAfterNDays(self, cells, n):


        dp = defaultdict(tuple)
        dp[n] = tuple(cells)
        t = defaultdict(int)
        t[tuple(cells)] = n
        print dp
        length = len(cells)
        pdb.set_trace()
        fast_forward = False
        while n > 0:
            n -= 1
            print "N:{}, ff:{}".format(n, fast_forward)
            if fast_forward:
                cells = dp[n]
            else:
                temp = []
                for i in xrange(length):
                    if i == 0 or i == length-1:
                        zero = 0 if cells[i] == 0 else 0
                        temp.append(zero)
                    else:
                        if (cells[i-1]==0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
                            temp.append(1)
                        else:
                            temp.append(0)

                #print temp
                dp[n] = tuple(temp)
                if t[tuple(temp)] > 0:
                    print "present:", n, temp
                    t[tuple(temp)] = n
                    fast_forward = True
                cells = temp
        print "Final:", cells
        return cells

a = Solution()
#a.prisonAfterNDays([0,1,0,1,1,0,0,1], 27)
a.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)
