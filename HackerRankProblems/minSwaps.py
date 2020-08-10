import pdb
from collections import defaultdict

class Solution(object):

    def minSwaps(self, grid):
        print "********"
        n = len(grid)
        arr = []
        if n == 1:
            return -1

        if n == 2:
            if grid[0][1] == 0:
                return 0
            if grid[1][1] == 0:
                return 1
            return -1

        zeros = defaultdict(int)

        for i in xrange(n):
            count = 0
            #pdb.set_trace()
            for j in reversed(xrange(n)):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            arr.append(count)
            zeros[tuple(grid[i])] = count

        print "Zeros:", zeros
        freq = zeros.values()
        freq = sorted(freq)
        print "freq:", freq

        if len(freq) < n-1:
            return -1
        for i in xrange(len(freq)):
            if freq[i] >= i:
                continue
            else:
                return -1

        print "to sort:", arr
        swap = 0
        for i in xrange(len(arr)):
            for j in xrange(0, len(arr)-i-1):
                if arr[j] < arr[j+1]:
                    swap += 1
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        print swap
        return swap




a = Solution()
print a.minSwaps([[0,0,1],[1,1,0],[1,0,0]])
print a.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])
print a.minSwaps([[1,0,0],[1,1,0],[1,1,1]])
