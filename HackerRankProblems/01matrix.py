import pdb

class Solution(object):

    def updateMatrix(self, matrix):

        def get_neighbours(ver, hor):
            result = []
            for v, h in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                indexi, indexj = ver+v, hor+h
                if ((indexi >= 0 and indexi < self.vertical) and (indexj >=0 and indexj < self.hori)):
                    result.append((indexi, indexj))
            return result

        self.vertical = len(matrix)
        if self.vertical < 1:
            return matrix

        self.hori = len(matrix[0])
        self.queue =[]
        for i in xrange(self.vertical):
            for j in xrange(self.hori):
                if matrix[i][j] == 0:
                    self.queue.append((i,j))

        print "initial:", self.queue

        self.visited = {}

        while len(self.queue) > 0:


            node = self.queue.pop(0)
            if not self.visited.get(node, False):
                ver, hor = node[0], node[1]
                if matrix[ver][hor] <> 0:
                    neighbours = get_neighbours(ver, hor)
                    min_val = min([matrix[i][j] for i, j in neighbours])
                    matrix[ver][hor] = min_val + 1
                for v, h in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    iindex, jindex = ver+v, hor+h
                    if ((iindex >= 0 and iindex < self.vertical) and (jindex >=0 and jindex < self.hori)):
                        self.queue.append((iindex, jindex))
                self.visited[(ver, hor)] = True
        print "final:", matrix
        print "visited:", self.visited
        return matrix

a = Solution()
a.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
