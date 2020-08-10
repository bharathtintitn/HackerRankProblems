import pdb
from collections import defaultdict

class Node(object):

    def __init__(self, val, l):

        self.val = val
        self.children = []
        self.label = l
        self.child_label = defaultdict(int)

class Solution(object):

    def __init__(self):

        self.graph = defaultdict(list)
        self.visited = defaultdict(bool)
        self.all_node = defaultdict(bool)

    def create_graph(self, edges, labels):

        for edge in edges:
            s, d = edge[0], edge[1]
            if not self.all_node[s]:
                l = labels[s]
                n = Node(s, l)
                self.all_node[s] = n
            else:
                n = self.all_node[s]
            if not self.all_node[d]:
                l = labels[d]
                m = Node(d, l)
                self.all_node[d] = m
            else:
                m = self.all_node[s]
            self.graph[s].append(m)
            self.graph[d].append(n)

    def countSubTrees(self, n, edges, labels):
        print "**************"
        self.create_graph(edges, labels)
        print "Graph:", self.graph
        self.result = [0]*n
        print "Before:", self.result
        self.dfs(0)
        print "After:", self.result

    def dfs(self, root):
        chara = defaultdict(int)
        if not self.visited[root]:
            self.visited[root] = True
            node = self.all_node[root]
            l = node.label
            chara[l] += 1
            for neig in self.graph[root]:
                ret = self.dfs(neig.val)
                for key, value in ret.iteritems():
                    chara[key] += value
            node.child_label = chara
            self.result[root] = chara[l]

        return chara



a = Solution()
a.countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab")
a = Solution()
a.countSubTrees(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa")
a = Solution()
a.countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa")


