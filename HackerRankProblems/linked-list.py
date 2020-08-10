class Node(object):

    def __init__(self, val):
        self.info = val
        self.next = None


class linked_list(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, val):

        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            return
        curr = self.tail
        curr.next = node
        self.tail = node
        self.length += 1


    def delete(self, val):

        import pdb
        #pdb.set_trace()
        curr = self.head
        prev = None
        while curr and curr.info != val:
            prev = curr
            curr = curr.next

        if curr.info == val:
            if not prev:
                prev = curr.next
            else:
                prev.next = curr.next
            curr.next = None
            self.length -= 1
        else:
            return

        if self.tail == curr:
            self.tail = prev

        if self.head == curr:
            self.head = prev

    def display(self):
        items = []
        curr = self.head
        while curr:
           print curr.info
           items.append(curr.info)
           curr = curr.next
        print items

    def size(self):

        return self.length


a = linked_list()
print a.size()

a.add(10)
a.add(20)
a.add(30)
a.add(40)
a.display()
print a.size()

a.delete(30)
print a.size()
print "Delete 40"
a.delete(40)
a.display()
print 'delete 10'
a.delete(10)
print 'delete 20'
a.delete(20)
print a.size()
