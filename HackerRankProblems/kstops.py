import pdb
class Solution(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		def get_graph():
			#graph = [[float('inf')]*n]*n
			#print graph

			#for edge in flights:
			#	print "edge:", edge
			#	print edge[0], edge[1], edge[2]
			#	pdb.set_trace()	
			#	graph[edge[0]][edge[1]] = edge[2]
			graph = {}
			for edge in flights:
				if graph.get(edge[0], False):
					graph[edge[0]][edge[1]] = edge[2]
				else:
					graph[edge[0]] = {}
					graph[edge[0]][edge[1]] = edge[2]

			print graph
		graph = get_graph()

		visited = set()
		queue = []
		for q in xrange(n):
			if q == src:
				queue.append((q,0),)
			else:
				queue.append((q, float('inf')),)
		print "Q:", queue

		path = []

a = Solution()
a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
