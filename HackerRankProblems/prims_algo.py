'''
'''
from heapq import heappush, heappop



class Prism(object):
    ''' Prism Algorithm Implementation'''

    def __init__(self, size):

        self.visited = [False for i in xrange(size+1)]
        self.graph = {}
        self.priority_queue = []
        self.final_graph = []
        self.graph_dict = {i:{} for i in xrange(size+1)}
        self.path = [None for i in xrange(size+1)]
        self.weight = [None for i in xrange(size+1)]

    def __lt__(self, x, y):
        return True if (x[2] < y[2]) else (not x[2] < y[2])

    def add(self, row):
        try:
            self.graph[row[0]].append((row[0],row[1],row[2]))
            d = self.graph_dict[row[0]]
            d[row[1]] = row[2]
        except:
            self.graph[row[0]] = [(row[0],row[1],row[2])]
            d = self.graph_dict[row[0]]
            d[row[1]] = row[2]
 
        try:
            self.graph[row[1]].append((row[1],row[0],row[2]))
            d = self.graph_dict[row[1]]
            d[row[0]] = row[2]
        except:
            self.graph[row[1]] = [(row[1],row[0],row[2])]
            d = self.graph_dict[row[1]]
            d[row[0]] = row[2]

    def calculate(self, source, node):
        '''Update the path and distance matrix of graph'''
        #print "In calu ",source, node

        if self.weight[node[1]] and self.weight[node[1]] > (self.weight[source] + node[2]):
            self.weight[node[1]] = self.weight[source] + node[2]
            self.path[node[1]] = source
        elif self.weight[node[1]] is None:
            self.weight[node[1]] = self.weight[source] + node[2]
            self.path[node[1]] = source

        #print 'weight ', self.weight
        #print 'path ', self.path

    def algo(self):

        import pdb
        vertex = self.source
        self.visited[0] = True
        self.weight[vertex] = 0

        while False in self.visited:
            if not self.visited[vertex]:
                self.visited[vertex] = True
                for node in self.graph[vertex]:
                    heappush(self.priority_queue, node)

            if len(self.priority_queue) <= 0:
                return

            #print "queue ", self.priority_queue
            node = heappop(self.priority_queue)
            #print "node is ", node
            self.calculate(node[0], node)
            vertex = node[1]

        #print "path is ", self.path
        #print "weight is ", self.weight

    def total(self):

        #print "inside total"
        total_weight = 0
        #print "graph", self.graph_dict

        for i,j in enumerate(self.path):
            #print "i, j", i, j
            if j:
                weight = self.graph_dict[i][j]
                #print "weight ", weight
                total_weight += weight

        #print "total weight", total_weight
        print total_weight

if __name__=="__main__":

    row = map(int, raw_input().strip().split())
    vertex, edges = row[0], row[1]
    #print "vertex ", vertex, " ","edge ", edges
    a = Prism(vertex)
    for _ in xrange(edges):
        row = map(int, raw_input().strip().split())
        a.add(row)
    #print a.graph
    a.source = int(raw_input().strip())
    #print a.source
    a.algo()
    a.total()
    #print a.final_graph

