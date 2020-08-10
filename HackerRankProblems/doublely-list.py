





class Node(object):

    def __init__(self, val):
        self.info = val
        self.next = None
        self.prev = None


class DoubleLL(object):


    def __init__(self):

        self.head = None
        self.count = 0

    def add(self, val):

        node = Node(val)
        if not self.head:
            self.head = node
            self.count += 1
            return

        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.next

        node.prev = prev
        prev.next = node
        self.count += 1
        return

    def delete (self, val):

        curr = self.head
        prev = None
        while curr and curr.info != val:
            prev = curr
            curr = curr.next

        import pdb
        pdb.set_trace()
        if curr.info == val:
            if self.head.info == curr.info:
                self.head = curr.next
                curr.next = None
                return
            if curr.next:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            else:
                curr.prev.next = curr.next



    def size(self):

        pass

    def display(self):

        temp = []
        curr = self.head
        while curr:
            temp.append(curr.info)
            curr = curr.next

        print temp

a = DoubleLL()
a.display()
a.add(10)
a.display
a.add(20)
a.add(30)
a.add(40)
a.display()
a.delete(40)
a.display()
a.add(50)
a.display()
a.delete(20)
a.display()
a.delete(10)
a.display()
a.delete(30)
a.display()
a.size()
