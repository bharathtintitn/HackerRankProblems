


class Solution(object):

    def initial(self, numCourses, prereq):

        self.numCourses = numCourses
        self.graph = {}
        self.to_remove = {}
        self.createGraph(numCourses, prereq)
        self.visited = [False]*numCourses
        self.path = []

    def createGraph(self, n, prereq):

        for i in xrange(n):
            self.graph[i] = {}
            self.to_remove[i] = []
        for edge in prereq:
            self.graph[edge[0]][edge[1]] = {}
            self.to_remove[edge[1]].append(edge[0])

        print "Graph:", self.graph
        print "Remove:", self.to_remove

    def removeDependency(self, node):

        dependencyNodes = self.to_remove[node]
        print "DepNodes: ", dependencyNodes
        for n in dependencyNodes:
            if self.graph[n].get(node, -1) != -1:
                self.graph[n].pop(node)

        print "After removing:", self.graph

    def noDependency(self):
        dig = []
        for key, value in self.graph.iteritems():
            if len(value) == 0:
                if not self.visited[key]:
                    dig.append(key)
        print "Dig:", dig
        return dig

    def findpath(self):

        dig = self.noDependency()
        while len(dig) > 0:
            node = dig.pop()
            print "Going node: ", node
            self.visited[node] = True
            print "Completed course:", node
            self.removeDependency(node)
            self.path.append(node)

            if len(dig) == 0:
                dig = self.noDependency()

        print "Final Path:", self.path
        print "Visited: ", self.visited
        if len(self.path) == self.numCourses:
            return self.path
        return []

    def findOrder(self, numCourses, prereq):

        self.initial(numCourses, prereq)
        return self.findpath()




a = Solution()
a.findOrder(2, [[1,0]])
a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
