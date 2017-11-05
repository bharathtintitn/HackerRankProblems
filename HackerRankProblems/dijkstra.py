

import heapq as q
import pdb

class Heap(object):
    ''' Heap for sorting tuple inside list'''

    def __init__(self):

        self.heap = []

    def __cmp__(self, x ):
        pdb.set_trace()
        return True if x[1] < self.heap[1] else False

    def __le__(self, x):
        pdb.set_trace()
        return True if x[1] < y[1] else False

    def __lt__(self, x):
        pdb.set_trace()
        return True if self.heap[1] < x[1] else False

    def heappush(self, data):
        ''' Push item into heap '''
        pdb.set_trace()
        q.heappush(self.heap, data)

    def heappop(self):
        ''' Pops least weight item '''
        return q.heappop(self.heap)


if __name__ == "__main__":

    h = Heap()
    temp = [(10,1), (1, 4), (2, 5), (11, 4)]

    for i in temp:
        h.heappush(i)

    print "Heap is ", h.heap

    for i in xrange(4):
        print h.heappop()

