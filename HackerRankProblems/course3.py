import pdb
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
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
        cycle = 0
        max_cycle = 0
        while q:
            cycleLen = len(q)
            vertex = q.pop(0)
            node = vertex[1]
            g = graph[node]
            done = True
            print "node:", node, " ", g
            array = graph[node]
            length = len(array)
            index = 0
            while index < length:
                print "indx:", index, " array:", array
                v = array[index]
                if v in visited:
                    array.remove(v)
                    length -= 1
                else:
                    index += 1

            length = len(array)
            if length == 0:
                visited.add(node)
            else:
                q.append([length, node])
            #q = sorted(q)
            print "visited:", visited, " q:", q
            if cycleLen == len(q):
                cycle += 1
                if cycle == n:
                    return False
            else:
                cycle = 0
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
