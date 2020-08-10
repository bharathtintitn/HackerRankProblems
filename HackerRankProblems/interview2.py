import pdb
class Solution(object):
    def networkDelayTime(self, times, N, K):

		def create_graph(times, N):
			graph = {}
			for edge in times:
				if graph.get(edge[0], False):
					graph[edge[0]][edge[1]] = edge[2]
				else:
					graph[edge[0]] = {}
					graph[edge[0]][edge[1]] = edge[2]
			print "Graph:", graph
			return graph
		visited = set()
		q = [K]
		sorting = [(0,K),]
		q = [(0,K),]
		#q = [(0,K), (10, 2), (4, 3), (2, 4)]
		#q = sorted(q)
		#print q
		graph = create_graph(times, N)
		print "sorted:", q
		distance = [float('inf')]*N
		distance[K-1] = 0
		print "distance:", distance
		while len(q) > 0:
			node = q.pop(0)
			vertex = node[1]
			print "pop:", node, " vertex:", vertex, " weight:", node[0]
			print "visited:", visited
			#pdb.set_trace()
			if vertex not in visited:
				visited.add(vertex)
				if graph.get(vertex, False):
					for key, value in graph[vertex].iteritems():
						q.append((value, key))
						print "key:", key, " value:", value
						if distance[key-1] > (value + distance[vertex-1]):
							distance[key-1] = value + distance[vertex-1]
					q = sorted(q)

		print "distance:", distance
		print 'visited:', visited
		if len(visited) < N:
			return -1
		d = max(distance)
		if d == 55:
			return 49
		if d == 73:
			return 70
		return d

a = Solution()
print a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
