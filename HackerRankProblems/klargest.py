import pdb

class Solution(object):

    def __init__(self):

        self.heap = []
        self.length = 0

    def addElement(self, elem):

        self.heap.append(elem)
        self.length += 1
        self.heapify()

    def heapify(self):

        start = 0
        temp = None
        index = self.length-1
        pdb.set_trace()
        while index > start:
            parent = (index/2)
            if parent >= 0:
                child1 = (parent*2)
                if (parent*2)+1 <= self.length - 1:
                    child2 = (parent*2)+1
                    if self.heap[child1] > self.heap[child2]:
                        i = child1
                    else:
                        i = child2
                else:
                    i = child1

                if self.heap[parent] < self.heap[i]:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[i]
                    self.heap[i] = temp
                index = parent
            else:
                break
        print "Heap:", self.heap

    def findKthLargest(self, nums, k):
        for i in nums:
            self.addElement(i)

        print "final:", self.heap

        while k > 0:
            #item = self.heap.pop(0)A
            item = self.heap[0]
            last = self.heap[self.length-1]
            self.heap[0] = last
            self.heap.pop()
            self.length -= 1
            self.heapify()
            k -= 1

            print "Item:", item

        return item
a = Solution()
#print a.findKthLargest([3,2,1,5,6,4], 2)
#print a.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print a.findKthLargest([3,2,3,1,2,4,5,5,6], 4)



