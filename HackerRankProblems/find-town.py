from collections import defaultdict
class Solution(object):
	def findJudge(self, N, trust):
		"""
		:type N: int
		:type trust: List[List[int]]
		:rtype: int
		"""
		graph = defaultdict(list)
		result = set()
		count = 0
		stack = []
		visited = defaultdict(bool)
		path = defaultdict(list)
		for node in trust:
			graph[node[0]].append(node[1])

		print graph
		for i in xrange(1, N+1):
			stack.append(i)
			while len(stack) > 0:
				node = stack.pop()
				print "Going node: ", node
				if not visited[node]:
					visited[node] = True
					edges = graph[node]
					if not edges:
						print "No edge: ", node
						self.update_path(path, node)
					for vertex in edges:
							#if not visited[vertex]:
							path[vertex].append(node)
							stack.append(vertex)
				else:
					print "visited :", node
					print "path: ", path
					if len(path[node]) > 1:
						self.update_path(path, node, update=path[node][0])

		print "visited: ", visited
		print "stack: ", stack
		print "Path: ", path

	def update_path(self, path, node, update=None):
		print "Path: ", path
		print "node: ", node
		if not update:
			update = node
		import pdb
		pdb.set_trace()
		reached = path[node]
		print "Reached: ", reached
		start = reached.pop()
		while start:
			from_node = path[start]
			if from_node:
				next_node = from_node.pop()
				path[start].append(update)
				start = next_node
			else:
				path[start].append(update)
				start = None
			

a = Solution()
a.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
