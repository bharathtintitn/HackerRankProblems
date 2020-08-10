import pdb
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        print "********************"
        graph = {}
        def creategraph():
            for i in xrange(numCourses):
                graph[i] = []
            #pdb.set_trace()
            for edge in prerequisites:
                    #graph[edge[0]] = {edge[1]: True}
                    graph[edge[0]].append(edge[1])
                    node = graph[edge[1]]
                    if edge[0] in node:
                        print "Cycle is present ", edge[0], " ",edge[1]
                        return False, graph
            return True, graph
        ret, graph  = creategraph()
        if not ret:
            return False
        print "Graph:", graph
        visited = set()
        q = []
        for key, value in graph.iteritems():
            q.append([len(value), key])
        q = sorted(q)
        print "sorted:", q
        loop = {}
        while q:
            vertex = q.pop(0)
            node = vertex[1]
            g = graph[node]
            done = True
            print "node:", node, " ", g
            for key in graph[node]:
                print "key:", key
                if key not in visited:
                    q.append([0, key])
                    done = False
                    if not loop.get(key, False):
                        loop[key] = 1
                    else:
                        if loop[key] > 2:
                            return False
                        else:
                            loop[key] += 1
                    break
            if done:
                visited.add(node)
            else:
                q.append([0, node])
                if not loop.get(node, False):
                    loop[key] = 1
                else:
                    if loop[node] > 2:
                        return False
                    loop[node] += 1
            print "visited:", visited, " q:", q
        length = len(visited)
        print "length:", length
        if length == numCourses:
            return True
        return False
                    
a = Solution()
print a.canFinish(2, [[1,0],[0,1]])
print a.canFinish(2, [[1,0]])
print a.canFinish(3, [[1,0],[0,2],[2,1]])
#pdb.set_trace()
print a.canFinish(3, [[0,1],[0,2],[1,0]])
print a.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
