import pdb

'''
Implementing kruskals algo.
'''


'''
Create Union Find to detect loop in graph.
'''


class Union_Find(object):
    'Union Find to detect which set give set of vertices belongs to.'

    def __init__(self, number_of_vertices=0):
        self.vertices = []
        self.parent = []

        for i in xrange(number_of_vertices + 1):
            self.vertices.append(i)
            self.parent.append(None)

    def get_set(self, vertex):
        'return to which set vertex belongs to.'
        index = vertex
        parent = self.parent[index]
        result = parent
        while parent:
            parent = self.parent[parent]
            if parent:
                result = parent
        return result

    def _update(self, vertex, parent):

        value = self.parent[vertex]
        #print "value going to update is %s" % value
        while value:
            temp = self.parent[value]
            self.parent[value] = parent
            value = temp

    def set_set(self, vertex, parent):
        'assign the set number for given vertex'
        #pdb.set_trace()
        v_set = self.get_set(vertex)
        p_set = self.get_set(parent)
        #print "vertex {} set is {} and parent {} set is {}".format(vertex,v_set,parent,p_set)
        if not v_set and not p_set:
            if vertex > parent:
                self.parent[parent] = vertex
            else:
                self.parent[vertex] = parent
            return True
        if v_set == p_set or v_set == parent or p_set == vertex:
           return False
        else:
            if vertex > parent:
                self._update(parent,vertex)
                self.parent[parent] = vertex
            else:
                self._update(vertex, parent)
                self.parent[vertex] = parent
        #print "After changes parent is {}".format(self.parent)
        return True

    def __str__(self):
        return ",".join(map(str,self.parent))

def insertion_sort(array, length):
    'Sort the given list in ascending order'
    if length > 0:
        for i in xrange(1,length):
            x = array[i]
            j = i
            while j > 0 and x[2] < array[j-1][2]:
                array[j] = array[j-1]
                j -= 1
            array[j] = x


def kruskals_algo(array, v, e):

    a = Union_Find(v)
    count = 1
    total = 0
    for edge in array:
       #print "count is %d " % count
       if count == v:
           #print "all vertex are reached exit"
           break
       else:
           if a.set_set(edge[0], edge[1]):
               count += 1
               total += edge[2]

    #print "Final total is %d" % total
    print total


if __name__ == "__main__":

    alist = []
    row = map(int, raw_input().strip().split())
    v,e = row[0],row[1]
    #print v,e
    for _ in xrange(e):
        row = map(int, raw_input().strip().split())
        alist.append(row)
    #print "edges after input ",alist
    insertion_sort(alist, e)
    #print alist
    kruskals_algo(alist,v,e)
