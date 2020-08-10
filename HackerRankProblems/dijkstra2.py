from Queue import PriorityQueue as PQ

def create_graph(edges):
	graph = {}
	for edge in edges:
		if graph.get(edge[0], False):
			graph[edge[0]].append([edge[1],edge[2]])
		else:
			graph[edge[0]] = [[edge[1], edge[2]]]
		if graph.get(edge[1], False):
			graph[edge[1]].append([edge[0], edge[2]])
		else:
			graph[edge[1]] = [[edge[0], edge[2]]]

	print "Graph:", graph
	return graph

def shortestReach(n, graph, s):

	pq = PQ()
	source = s

	visited = {}

	stack = [source]
	count = 1

	#distance = [-1]*(n+1)
        distance = {}
	distance[source] = 0

	while count > 0:
                import pdb
                pdb.set_trace()
		print "count: ", count
		node = stack.pop()
                count -= 1
                if not visited.get(node): 
                    current_cost = distance[node]
                    #count -= 1
                    print "Node: ", node
                    node_reachable = graph[node]
                    print "Edges: ", node_reachable
                    for neighbour in node_reachable:
                            if not visited.get(neighbour[0]):
                                stack.append(neighbour[0])
                                count += 1
                                cost = distance.get(neighbour[0], 0)
                                if ((cost + current_cost) < distance.get(neighbour[0], 999999999999)):
                                   #(neighbour[1] + current_cost)):
                                   distance[neighbour[0]] = cost + neighbour[1]
                                print distance
                    visited[node] = 1
        print distance

if __name__ == "__main__":

    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()
        n = int(nm[0])
	print "n:",n
        m = int(nm[1])
	print "m:",m
        edges = []
        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))
	print "Edges:", edges
        s = int(raw_input())
	print "start:", s
	graph = create_graph(edges)
        result = shortestReach(n, graph, s)
