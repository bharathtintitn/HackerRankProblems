import pdb
from heapq import nlargest

class Solution(object):

    def findMaximizedCaptial(self, k, w, profit, captial):

        if w >= sum(captial):
            return sum(nlargest(k, profit))

        n = len(profit)
        index = -1
        for i in xrange(min(k, n)):

            for j in xrange(n):

                if captial[j] <= w:
                    if index == -1:
                        index = j
                    elif profit[j] > profit[index]:
                        index = j

            if index == -1:
                break
            w += profit[index]
            captial[index] = float('inf')
            index = -1

        print w
        return w

a = Solution()
print a.findMaximizedCaptial(2, 0, [1,2,3], [0,1,1])
