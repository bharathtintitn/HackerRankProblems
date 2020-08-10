import math

class Heap(object):

    def __init__(self):

        self.size = -1
        self.heap = []

    def swap(self, index1, index2):

        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        index = self.size
        print "Index: ", index
        if not index:
            return
        import pdb
        pdb.set_trace()
        parent = int(math.floor((index - 1)/2))
        print "Parent: ", parent
        while parent >= 0:
            if parent >= 0:
                if self.heap[parent] > self.heap[index]:
                    self.swap(parent, index)
                    index = parent
                else:
                    break
            else:
                break
            parent = int(math.floor((index - 1)/2))
            print "Parent: ", parent
        print "Heap: ", self.heap

    def delete(self, data):

        for i in xrange(self.size):
            if data == self.heap[i]:
                self.heap.pop(i)
                self.size -= 1
                return

    def getMin(self):
        if self.size > 0:
            index = 0
            data = self.heap[index]

            import pdb
            pdb.set_trace()
            while index <= self.size:
                child1 = (2*index)+1
                child2 = (2*index)+2
                if child2 > self.size:
                    if child1 > self.size:
                       self.heap.pop(index)
                    else:
                        self.swap(child1, index)
                        self.heap.pop(child1)
                    break
                else:
                    if self.heap[child2] < self.heap[child1]:
                        self.swap(child2, index)
                        index = child2
                    else:
                        self.swap(child1, index)
                        index = child1
        self.size -= 1
        return data 



if __name__ == "__main__":

    h = Heap()
    tests = int(raw_input().strip())
    for _ in xrange(tests):
        query = map(int, raw_input().split())
        if len(query) == 1:
            print h.getMin()
        if query[0] == 1:
            h.insert(query[1])

        elif query[0] == 2:
            h.delete(query[1])


