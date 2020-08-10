import pdb
from collections import defaultdict

class Solution(object):

    def criticalConnections(self, n, connections):

        graph = defaultdict(list)
        for v in connections:
            n1, n2 = v[0], v[1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        print "Graph:", graph

        dfn, low = [], []
        for i in xrange(n):
            dfn.append(None)
            low.append(None)

        self.cur = 0
        def dfs(node, parent):

            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for v in graph[node]:
                    if dfn[v] is None:
                        dfs(v, node)

                if parent is None:
                    l = min([low[i] for i in graph[node] + [low[node]]])
                else:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                print "low:{}, node:{}, parent:{}, low:{}, dfn:{}".format(l, node, parent, low, dfn)
                low[node] = l

        dfs(0, None)
        res = []
        print "Final low:{}, dfn:{}".format(low, dfn)
        for v in connections:
            v1, v2 = v[0], v[1]
            if low[v1] > dfn[v2] or low[v2] > dfn[v1]:
                res.append(v)
        print "res:", res
        return res

a = Solution()
a.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
