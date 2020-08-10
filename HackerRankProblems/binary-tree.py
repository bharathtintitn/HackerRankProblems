

class Node(object):

    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None



class BinaryTree(object):

    def __init__(self):
        self.root = None

    def getParent(self):

        curr = self.root
        queue = []
        queue.append(curr)
        while queue:
            temp = queue.pop(0)
            if not temp.left or not temp.right:
                return temp
            queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return None

    def insert(self, val):

        node = Node(val)
        if not self.root:
            self.root = node
            return

        parent = self.getParent()
        if not parent:
            print 'Could not find place to insert'
            return
        if not parent.left:
            parent.left = node
        else:
            parent.right = node

    def delete(self, val):
        pass

    def inorder(self, root):

        if not root:
            return

        self.inorder(root.left)
        print root.info
        self.inorder(root.right)

    def display(self):
        self.inorder(self.root)

    def _is_val_present(self, root, val):

        if not root:
            return False

        left = self._is_val_present(root.left, val)
        if root.info == val:
            return True
        right = self._is_val_present(root.right, val)
        return left or right

    def search(self, val):
        return self._is_val_present(self.root, val)

a = BinaryTree()
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.insert(50)
a.insert(60)
a.insert(70)
a.insert(80)
a.insert(90)
print a.search(50)
print a.search(100)
print a.search(60)
a.display()

