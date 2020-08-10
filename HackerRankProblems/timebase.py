''' Time based map. '''
import pdb
from collections import defaultdict

class Node(object):
    '''This is node.'''
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

class BinaryTree(object):
    '''this is binary tree.'''

    def __init__(self):
        self.root = None

    def add_node(self, key, val):
        ''' Add node to tree.'''
        node = Node(key, val)
        if not self.root:
            self.root = node
            return
        curr = self.root
        prev = None
        while curr:
            prev = curr
            if key == curr.key:
                curr = None
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if key == prev.key:
            prev.val = val
        elif key < prev.key:
            prev.left = node
        else:
            prev.right = node

    def inorder(self):
        '''Print binary tree.'''
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print "key: ", root.key, " value: ", root.val
            self._inorder(root.right)

    def search(self, key):
        '''Search node in tree.'''
        if not self.root:
            return None
        curr = self.root
        low = self.root
        high = self.root
        prev = None
        while curr:
            prev = curr
            if low.key < curr.key and curr.key < key:
                low = curr

            if high.key > curr.key and curr.key > key:
                high = curr

            if curr.key == key:
                return curr
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
            #if prev.key < key and curr.key > key:
            #    return prev
            #elif prev.key > key and curr.key < key:
            #    return curr
        if low.val > high.val:
            return high
        return low

a = BinaryTree()
pdb.set_trace()
a.add_node(10, 'z')
a.add_node(20, 'a')
a.add_node(30, 'a')
a.add_node(15, 'a')
a.add_node(5, 'b')
a.inorder()
print a.search(7).key
print a.search(19).key
print a.search(35).key
print a.search(3).key

dictionary = defaultdict(BinaryTree())
def create_dict(input1, input2):

    if input1 == "TimeMap":
        return

    if input1 == 'set':
        key = input2[0]
        value = input2[1]
        time = input2[2]
        dictionary[key].add_node(time, value)

    else:
        key = input2[0]
        time = input2[1]
        print dictionary[key].search(time).val
    


input_1 = ["TimeMap","set","get","get","set","get","get"]
input_2 = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

for i,j in zip(input_1, input_2):
    create_dict(i, j)
