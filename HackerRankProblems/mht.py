import pdb
import copy
from collections import defaultdict

class Solution(object):

    def findMinHeightTrees(self, n, edges):

        if n == 0:
            return []

        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        print "graph:", graph

        degree = defaultdict(int)
        queue = []
        for key, value in graph.iteritems():
            if len(value) == 1:
                queue.append(key)
            degree[key] += len(value)

        print "degree:", degree
        print "queue:", queue
        prev = []
        visited = defaultdict(bool)
        while queue:
            temp = []
            for node in queue:
                for row in graph[node]:
                    degree[row] -= 1
                    if degree[row] == 1:
                        temp.append(row)
            print "temp:", temp
            queue = temp
            if len(temp) > 0:
                prev = copy.deepcopy(temp)
                print "Prev:", prev
        print "final:", prev
        return prev 


a = Solution()
a.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
a.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
