import pdb
from collections import defaultdict

class Solution(object):

    def orangesRotting(self, grid):

        y = len(grid)
        if y == 0:
            return 0
        x = len(grid[0])

        q = []
        visited = defaultdict(bool)
        change = defaultdict(bool)
        for i in xrange(y):
            for j in xrange(x):
                if grid[i][j] == 2:
                    q.append((i,j,0),)
                if grid[i][j] == 1:
                    change[(i,j)] = True
                    #visited[(i,j)] = True

        print "initial q:{}, visited:{}".format(q, visited)


        def bfs():

            def isValid(a, b):
                if ((a >= 0 and a < y) and (b >= 0 and b < x)):
                    return True
                return False

            maxDays = 0
            while q:
                print "q:", q, " visited:",visited
                node = q.pop(0)
                indexi, indexj, count = node[0], node[1], node[2]
                if not visited[(indexi, indexj)]:
                    visited[(indexi, indexj)] = True
                    for v1, v2 in ((-1,0), (1,0), (0, 1), (0, -1)):
                        nexti, nextj = indexi+v1, indexj+v2
                        if isValid(nexti, nextj):
                            if grid[nexti][nextj] == 1 and not visited[(nexti, nextj)]:
                                q.append((nexti, nextj, count+1),)
                                grid[nexti][nextj] = 2
                                change[(nexti, nextj)] = False
                                if maxDays < count+1:
                                    maxDays = count+1

            for key, value in change.iteritems():
                if value:
                    return -1

            print "max days:", maxDays

            return maxDays

        return bfs()

a = Solution()
print a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
print a.orangesRotting([[0,2]])
