import pdb

from collections import deque

class Solution(object):

    def shortestPath(self, grid, k):

        m = len(grid)-1
        if m < 0:
            return -1
        n = len(grid[0]) - 1

        q = deque([(0, 0, k, 0)])
        visited = set([(0,0)])

        def isValid(i, j):

            if (i >=0 and i <= m) and (j >= 0 and j <= n):
                return True
            return False

        while q:

            row, col, obs, steps = q.popleft()
            print "row:{}, col:{}, obs:{}, steps:{}".format(row, col, obs, steps)

            for i, j in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:

                if isValid(i,j) and (i,j) not in visited:
                    if grid[i][j] == 1 and obs > 0:
                        q.append((i,j,obs-1,steps+1))
                    if grid[i][j] == 0:
                        q.append((i,j,obs,steps+1))
                    if i == m and j == n:
                        return steps + 1
                    visited.add((i, j))

        return -1

a = Solution()
print a.shortestPath([[0,0,0],
     [1,1,0],
     [0,0,0],
     [0,1,1],
     [0,0,0]],1)
