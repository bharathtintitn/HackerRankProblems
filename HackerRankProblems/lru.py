'''LRU'''

class Node(object):
    '''Node class.'''

    def __init__(self, val, key):
        self.prev = None
        self.val = val
        self.key = key
        self.next = None

class LFUCache(object):
    '''LRU'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.hashmap = {}
        self.head = None
        self.tail = None

    def get(self, key):
        '''Return item.'''
        print "Get: ", key
        if self.hashmap.get(key, False):
            node = self.hashmap[key]
            self.update(key, node.val,  node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        ''' put item.'''
        print "Put: ", key, " ", value
        if self.hashmap.get(key, False):
            self.update(key, value, node)
        else:
            self.insert(key, value)

        self.display()

    def display(self):
        '''Display hashmap.'''
        start = self.head
        while start:
            print "key: ", start.key, " val: ", start.val
            start = start.next

    def insert(self, key, val):
        node = Node(val, key)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1
        if self.length > self.capacity:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
            remove = self.hashmap.pop(temp.key)
            print "Remove key: ",temp.key, " value:", temp.val 
        self.hashmap[key] = node

    def update(self, key, val, node):

        self.hashmap[key] = node
        node.val = val
        previous = node.prev
        next_node = node.next

        if self.head == node:
            if not self.head.next:
                self.head = self.head.next
                self.head.prev = None
                node.next = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.head = node
                self.tail = node
        else:
            if not next_node:
                next_node.prev = previous
                node.prev = None
                previous.next = next_node
                node.next = None
                self.tail.next = node
                node.prev = self.tail

obj = LFUCache(capacity);
print obj.get(key)
obj.put(key,value);

