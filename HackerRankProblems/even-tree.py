'''
You are given a tree (a simple connected graph with no cycles). The tree has  nodes numbered from  to  and is rooted at node .

Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of vertices.

Input Format

The first line of input contains two integers  and .  is the number of vertices, and  is the number of edges. 
The next  lines contain two integers  and  which specifies an edge of the tree.

Constraints

Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.

Output Format

Print the number of removed edges.

Sample Input

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
Sample Output

2
Explanation

On removing edges  and , we can get the desired result.
'''

graph = {}
remove_edge = 0
total = 0

def dfs(source, destination, graph):
    '''This is dfs graph algorithm.'''
    global remove_edge
    total = 0
    count = 0
    for node in graph[source]:
        if node != destination:
            count = dfs(node, source, graph)
            if count != 0 and count%2 == 0:
                remove_edge += 1
            total += count

    return max(total+1, 1)

def add_edge(source, dest):
    ''' Add edges to given graph.'''
    try:
        graph[source].append(dest)
    except:
        graph[source] = [dest]
    try:
        graph[dest].append(source)
    except:
        graph[dest] = [source]



if __name__ == "__main__":

    row = map(int, raw_input().strip().split())
    n, m = row[0], row[1]
    #print m,m
    for _ in xrange(m):
        row = map(int, raw_input().strip().split())
        add_edge(row[0], row[1])

    #print "Going to call dfs.. be ready"
    #import pdb
    #pdb.set_trace()
    dfs(row[0], None, graph)
    print remove_edge
    #print graph
