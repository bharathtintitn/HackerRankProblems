class Solution(object):

    def create_graph(self, route):
		graph = {}
                sector = {}
		for path in route:
			for i in path:
				if not graph.get(i, False):
					graph[i] = []
                                        sector[i] = ["".join(map(str, path))]
                                else:
                                    sector[i].append("".join(map(str, path)))
			for i in path:
				graph[i].extend(path)
		return graph, sector

    def bfs(self, graph, source, target, sector):
		visited = {}
		path = {}
                path[source] = None
		stack = [source]
                max_total = 99999
                total = -1

		while len(stack) > 0:
			item = stack.pop()
			print "item:", item
			visited[item] = True
			vertex = graph[item]
			print "Vertex:", vertex
			if item == target:
                            route = self.get_count(path, source, target)
                            print "Route:", route
                            total = self.get_sum(route, sector, path)
                            print "total:", total
                            if max_total > total:
                                max_total = total
			for node in vertex:
				if not visited.get(node, False):
					stack.append(node)
					path[node] = item
		return max_total if max_total <> 99999 else total

    def get_sum(self, route, sector, path):
        sector_set = set()
        for i in route:
            if len(sector[i]) > 1:
                sec = sector[i]
                source = sector[path[i]]
                for s in sec:
                    if s in source:
                        sector_set.add(s)
            else:
                sector_set.add(sector[i][0])
        print "sector set:", sector_set
        return len(sector_set)

    def get_count(self, path, s, t):
		item = t
		route = [item]
		while item <> s:
			item = path[item]
			route.append(item)
		return route

    def numBusesToDestination(self, routes, S, T):
		"""
		:type routes: List[List[int]]
		:type S: int
		:type T: int
		:rtype: int
		"""
		graph, sector = self.create_graph(routes)
		print graph
                print sector
		path = self.bfs(graph, S, T, sector)
		print "Path:", path
		#print self.get_count(path, S, T)

a = Solution()
a.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)
