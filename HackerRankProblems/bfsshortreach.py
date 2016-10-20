import sys
import Queue as q

class Edge(object):

  def __init__(self, vertexOne, vertexTwo, weight):
    self._vertexOne = vertexOne
    self._vertexTwo = vertexTwo
    self._weight = weight


  def sort_edge(self, edge_list):
    pass


class Graph(object):

  def __init__(self, direction=True):
    self.graph = {}
    self.directed = direction
    self.edges = []

  def add(self, v1, v2, weight):

    if self.directed:
      self.add_node(v1, v2, weight)
      self.add_node(v2, v1, weight)
    

  def add_node(self, v1, v2, weight):
    if v1 in self.graph:
      self.graph[v1].append((v2,weight))
    else:
      self.graph[v1] = [(v2, weight)]

    if v2 not in self.graph:
      self.graph[v2] = []

  def print_graph(self):
    for node,reachable in self.graph.iteritems():
      print "Node: {} --> {}".format(node,reachable)

  def sort_edges(self):
    for node, reachable in self.graph.iteritems():
      for i in reachable:
        self.edges.append(Edge(node,i[0],i[1]))
        print "{} to {} costs {}".format(node,i[0],i[1])

    self.edge.sort_edge(self.edges)    

def sort(array):
  length = len(array)
  for i in xrange(length):
    swap = False
    for j in xrange(length - 1):
      if array[j+1][1] < array[j][1]:
        temp = array[j+1]
        array[j+1] = a[j]
        a[j] = temp
        swap = True

    if not swap:
      break

  return array

def update_distance(array, index, value):

  for i in array:
    if i[0] == index:
      i[1] = value
      return array

  return array

def dijkstra(graph, source, n):
  
 visited = [False]*(n+1)
 #print "visited", visited
 distance = [-1]*(n+1)

 stack = [source]
 queue = list()
 queue = [(source,0)]
 distance[source] = 0

 #print "Stack {}, q {}".format(stack, queue)

 while len(queue) > 0:

   node = queue.pop(0)
   #print "Going for node {}".format(node)
   visited[node[0]] = True

   for item in graph[node[0]]:
     #print "node {} --> {}:{}".format(node, item[0], item[1])
     dist = distance[node[0]] + item[1]
     if distance[item[0]] == -1:
       distance[item[0]] = dist 
       try:
        if not visited[item[0]]:
          queue.append((item[0],dist))
       except:
        if not visited[item[0]]:
         queue = [(item[0], dist)]

     elif distance[item[0]] > dist: 
       distance[item[0]] = dist
       queue = update_distance(queue, item[0], dist)

     queue = sort(queue) 
 for i in xrange(1,n+1):
   if i == 0 or i == source:
     continue
   print distance[i],
 print ""



def main():


  N = int(raw_input().strip())

  for _ in xrange(N):
    g = Graph()
    intial_values = map(int, raw_input().strip().split())
    n,m = intial_values[0], intial_values[1]

    for _ in xrange(m):
      row = map(int, raw_input().strip().split())
      g.add(row[0],row[1],6)

    source = int(raw_input().strip())
    dijkstra(g.graph,source,n)

if __name__ == '__main__':

  main()
