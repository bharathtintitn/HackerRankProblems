import pdb


def add_edge(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)


def create_graph(edges, n):

    graph = {i:[] for i in xrange(n)}
    #print("Graph:{}".format(graph))
    for edge in edges:
        add_edge(graph, edge[0], edge[1])

    #print('Final Graph:{}'.format(graph))
    return graph

def dfs(graph, source, visited):

    path = []
    stack = []
    stack.append(source)
    count = 1
    while count > 0:
        node = stack.pop(count-1)
        count -= 1
        #print('Node:{}'.format(node))
        if not visited[node]:
            path.append(node)
            #print('Node {} is not visited'.format(node))
            visited[node] = True
            reachable = graph[node]
            #print('Reachable:{}'.format(reachable))
            for vertex in reachable:
                stack.append(vertex)
                count += 1

    #print('Path visited:{}'.format(path))
    return path

if __name__ == "__main__":

    n, p = tuple(map(int, raw_input().split()))
    edges = set()
    for _ in xrange(p):
        edges.add(tuple(map(int, raw_input().split())))

    #print('N:{}, P:{}'.format(n, p))
    #print('Nationality:{}'.format(edges))
    graph = create_graph(edges, n)
    visited = {i:False for i in xrange(n)}
    source = 0
    result = 0
    reachable_path = []
    for source in xrange(n):
        path = dfs(graph, source, visited)
        #print("Path========>{}".format(path))
        length = len(path)
        if length > 0:
            reachable_path.append(length)
    #print("Path:{}".format(reachable_path))
    total = 0
    for size in reachable_path:
        result += total * size
        total += size

    #print('Result:{}'.format(result))
    print(result)

