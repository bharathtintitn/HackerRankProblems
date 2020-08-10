import pdb
import heapq as heap
from collections import defaultdict, deque

class Solution(object):


    def __init__(self):

        self.n = 0
        self.graph = defaultdict(list)
        self.visited = defaultdict(bool)
        self.distance = defaultdict(int)
        self.parent = defaultdict(None)
        self.max_total = 0.0
        self.h = []

    def create_graph(self, edges, succProb):
        for i, edge in enumerate(edges):
            self.graph[edge[0]].append([edge[1], succProb[i]])
            self.graph[edge[1]].append([edge[0], succProb[i]])
            self.distance[edge[0]] = float('inf')
            self.distance[edge[1]] = float('inf')

        print "Graph:", self.graph
    '''
    def maxProbability(self, n, edges, succProb, start, end):

        self.n = n
        self.create_graph(edges, succProb)
        pdb.set_trace()
        self.dfs(start, end, None)
        print "max:", self.max_total
        return self.max_total
    '''
    def maxProbability(self, n, edges, succProb, start, end):

        self.n = n
        self.create_graph(edges, succProb)
        pdb.set_trace()
        print "Distance:", self.distance
        print "Parent:", self.parent
        self.distance[start] = 0
        self.q = deque([])
        self.q.append(start)
        self.h = [[0.0, start]]
        heap.heapify(self.h)
        while self.h:
            #node = self.q.popleft()
            dist, node = heap.heappop(self.h)
            print "Node:", node
            self.visited[node] = True
            print "Dist:{}, node:{}, visited:{}, max:{}, h:{}".format(dist, node, self.visited, self.max_total, self.h)
            if node == end:
                if dist < self.max_total:
                    self.max_total = dist
            if dist == 0.0:
                dist = -1.0
            for nei, prob in self.graph[node]:
                if not self.visited[nei]:
                    self.q.append(nei)
                    heap.heappush(self.h, [-1*(prob*(-1*dist)), nei])


        print "max:", self.max_total
        return self.max_total*-1

    '''
    def dfs(self, start, end, total):

        if start == end:
            if total is None:
                if self.max_total == 0.0:
                    total = 0.0
                else:
                    total = 1.0
            if total > self.max_total:
                self.max_total = total
            return
        if total is None:
            total = 1.0
        self.visited[start] = True
        for node, prob in self.graph[start]:
            if not self.visited[node]:
                self.dfs(node, end, total*prob)
    '''



a = Solution()
a.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)
a = Solution()
a.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)
a = Solution()
a.maxProbability(3, [[0,1]], [0.5], 0, 2)


