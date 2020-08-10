import pdb
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
		print "********************"
		graph = {}
		def creategraph():
			for i in xrange(numCourses):
				graph[i] = {}
			#pdb.set_trace()
			for edge in prerequisites:
					graph[edge[1]] = {edge[0]: True}
					node = graph[edge[0]]
					if node.get(edge[1], False):
						print "Cycle is present ", edge[0], " ",edge[1]
						return False, graph
			return True, graph
		ret, graph  = creategraph()
		if not ret:
			return False
		print "Graph:", graph
		visited = set()
		source = None
		minlen = float('-inf')
		for key, value in graph.iteritems():
			if minlen < len(value):
				source = key
				minlen = len(value)
		q = []
		if source <> None:
			q.append(source)
		print "source:", source, " q:", q
		while q:
			node = q.pop(0)
			visited.add(node)
			g = graph[node]
			print "node:", node, " ", g
			for key, value in graph[node].iteritems():
				if key not in visited:
					q.append(key)
		length = len(visited)
		print "length:", length
		if length == numCourses:
			return True
		return False
				
			
a = Solution()
print a.canFinish(2, [[1,0],[0,1]])
print a.canFinish(2, [[1,0]])

