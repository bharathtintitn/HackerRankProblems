import pdb
from typing import List
from collections import deque

class Solution(object):

    def findOrder(self, num: int, prereq: List[List[int]]) -> List[int]:

        if not prereq:
            return []
        graph = {}
        for i in range(num):
            graph[i] = [[],[]]

        print("Graph:", graph)
        for edge in prereq:
            source, dest = edge[1], edge[0]
            graph[source][1].append(dest)
            graph[dest][0].append(source)
        print("Final Graph:", graph)

        q = deque([])
        for key, value in graph.items():
            if len(value[0]) == 0:
                q.append(key)

        print("Q:", q)
        result = []
        while q:
            node = q.popleft()
            print("Node selected:", node)
            result.append(node)
            neigh = graph[node][1]
            for nei in neigh:
                graph[nei][0].remove(node)
                if len(graph[nei][0]) == 0:
                    q.append(nei)

        print("Final result:", result)
        return result

a = Solution()
assert a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0,1,2,3], [0,2,1,3]]
assert a.findOrder(2, [[1,0]])
