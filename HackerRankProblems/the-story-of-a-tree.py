from fractions import gcd


def verifyParent(parent, guesss, k):
	#print "Parent:", parent
	#print "guess:", guesss
	for g in guesss:
		if parent[g[1]] != g[0]:
			#print '*********',parent[g[1]], ' ', g[0]
			return False
	#print "######## PASS"
	return True

def dfs(graph, source):

	visited = {}
	parent = {}
	parent[source] = 9999999999999 
	stack = []
	count = -1
	stack.append(source)
	count += 1
	while count >= 0:
		#print "Count:", count
		pop = stack.pop(count)
		count -= 1
		#print "Pop:", pop
		#print "Parent:", parent
		if not visited.get(pop,False):
			visited[pop] = True
			node_list = graph[pop]
			#print "Node List:", node_list
			for node in node_list:
				stack.append(node[1])
				count += 1
				if not parent.get(node[1], False):
					parent[node[1]] = pop
		#isClear(parent)
	#print "Final Parent:", parent
	return parent


def storyOfATree(n, edges, k, guesses):

	graph = {}
	for edge in edges:
		if not graph.get(edge[0], False):
			graph[edge[0]] = [(edge[0], edge[1])]
		else:
			graph[edge[0]].append((edge[0],edge[1]))

		if not graph.get(edge[1], False):
			graph[edge[1]] = [(edge[1], edge[0])]
		else:
			graph[edge[1]].append((edge[1], edge[0]))

	#print "Graph:", graph
	won = 0
	for i in xrange(n):
		parent = dfs(graph, i+1)
		toEnd = verifyParent(parent, guesses, k)
		if toEnd:
			#print "Won:", won
			won += 1
	gcdis = gcd(won, n)
	won = won/gcdis
	n = n/gcdis
	return str(won) + '/' + str(n)

if __name__ == "__main__":

    edge_list = []
    T = int(raw_input().strip())
    #print "T:",T
    for _ in xrange(T):
        number_of_node = int(raw_input().strip())
        #print "Number of node:", number_of_node
        for _ in xrange(number_of_node  - 1):
            edge = map(int, raw_input().strip().split())
            edge_list.append(edge)

        #print "Edges:", edge_list


	gk = raw_input().split()

        g = int(gk[0])

        k = int(gk[1])

        guesses = []

        for _ in xrange(g):
            guesses.append(map(int, raw_input().rstrip().split()))
	#print "guess:",guesses

        result = storyOfATree(number_of_node, edge_list, k, guesses)
	print "result:", result
