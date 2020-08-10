class Q(object):

    def __init__(self,size):

        self.size = size
        self.q = [None]*size
        self.front = -1
        self.rear = -1

    def push(self, data):
        if not self.isOverflow():
            self.front += 1
            self.q[self.front] = data
            if self.front == self.size - 1:
                self.front = 0
            if self.rear == -1:
                self.rear = 0
            print "Front is at:", self.front
        else:
            print "Q is overflow:", self.q

    def pop(self):

        if not self.isUnderflow():
            item = self.q[self.rear]
            self.q[self.rear] = None
            self.rear += 1
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            if self.rear == self.size:
                self.rear = -1
            print "Item poped:", item
            print "rear is at:", self.rear
        else:
            print "Q is underflow:", self.q

    def isOverflow(self):
        diff = abs(self.front - self.rear)
        if diff == 0:
            return True
        return False

    def isUnderflow(self):

        total = self.front + self.rear
        if self.front == self.rear:
            return True
        return False



if __name__ == "__main__":

    a = Q(5)
    import pdb
    pdb.set_trace()
    a.push(5)
    print a.q
    a.push(4)
    print a.q
    a.push(3)
    print a.q
    a.pop()
    print a.q
    a.pop()
    print a.q
    a.pop()
    print a.q
    a.pop()
    print "Expecting underflow"
    print a.q
    a.push(10)
    print a.q
    a.push(11)
    print a.q
    a.push(12)
    print a.q
    a.push(13)
    print a.q
    a.push(14)
    print a.q
    a.push(15)
    print a.q
    a.push(16)
    print a.q
    a.pop()
    print a.q
    
