import pdb

class Heap(object):
    ''' This is heap :) '''

    def __init__(self):
        self.heap = []

    def add(self, data):
        ''' Add item to heap. '''


        start = 0
        self.heap.append(data)
        pos = len(self.heap)
        self._add(start, pos-1)

    def _add(self, start, pos):

        temp = self.heap[pos]
        pdb.set_trace()
        while start < pos:
            parent = pos >> 1
            print "Parent is {} and item is {}".format(parent, self.heap[parent])
            if self.heap[parent] > self.heap[pos]:
                self.heap[pos] = self.heap[parent]
                self.heap[parent] = temp
                temp = self.heap[parent]
                pos = parent
            else:
                break
        self.heap[pos] = temp

    def pop(self):

        length = len(self.heap)
        if length == 0:
            return
        else:
            item = self.heap.pop()
            return item

if __name__ == "__main__":

    a = [9, 8, 1, 5, 6]
    a = [1, 2, 3,4, 5]
    a = [2, 1]
    a = [1]
    h = Heap()
    for i in a:
        h.add(i)
    print h.heap
