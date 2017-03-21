

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

    def set_set(self, vertex, parent):
        'assign the set number for given vertex'
        v_set = self.get_set(vertex)
        p_set = self.get_set(parent)
        print "vertex {} set is {} and parent {} set is {}".format(vertex,v_set,parent,p_set)
        if v_set == p_set:
            pass
        else:
            if vertex > parent:
                self.parent[parent] = vertex
            else:
                self.parent[vertex] = parent
