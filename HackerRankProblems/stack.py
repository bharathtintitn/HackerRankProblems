

import pdb


class Stack(object):

    def __init__(self, size):

        self.top = -1
        self.stack = [None]*size
        self.size = size


    def push(self, item):
        '''Push item to stack'''

        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print "Stack is overflow"

    def pop(self):
        '''Remove top item from stack.'''
        if self.top < 0:
            print "Stack is underflow"
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item


    def __repr__(self):
        print "Here in repr"
        return 'Elements in stack: {}'.format(self.stack)

    def __str__(self):
        print 'Here in str'
        return 'Elements in stack: {}'.format(self.stack)


if __name__ == '__main__':

    s = Stack(5)
    print s
    s.push(1)
    s.push(30)
    print s
    s.push(29)
    print s
    s.pop()
    s.pop()
    s.push(3)
    s.push(4)
    s.push(5)
    print s
    s.push(8)
    print s
    s.push(9)
    print s
    for i in xrange(6):
        print s.pop()



