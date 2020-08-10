
def dfs(g, i, visited, ordering, index):

    visited[i] == True
    row = g[i]
    for node in row:
        if not visited[node]:
            dfs(g, node, visited, ordering, index)
    ordering[index] = i
    print "Index: ", index, " i:", i,
    index -= 1

def topsort(g):

    length = len(g)
    visited = [False]*length
    ordering = [None]*length
    index = length - 1

    for i in xrange(length):
        if not visited[i]:
            index = dfs(graph, i, visited, ordering, index)

    print "sort: ", ordering

graph = {0: [], 1:[0], 2:[1], 3:[1], 4:[], 5:[2,4], 6:[3,4], 7:[5,6]}
print "Graph:", graph
topsort(graph)
