import pdb
import copy

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):

        self.n = 0
        self.output = {}
        self.order = []
        self.count = 0

    def perOrder(self, root):

        if not root:
            return None
        self.order.append(root.val)
        self.order.append(self.perOrder(root.left))
        self.order.append(self.perOrder(root.right))

    def generate_nodes(self):
        self.map = {}
        for i in xrange(1, self.n+1):
            node = TreeNode(i)
            self.map[i] = [False, node]

    def binarySearchTree(self, node, addNode):

        if node.val > addNode.val:
            node.left = addNode
        else:
            node.right = addNode
        return addNode

    def dfs(self, root, source):

        if not source:
            return
        if self.count >= self.n:
            #pdb.set_trace()
            self.perOrder(root)
            print self.order
            self.output[tuple(self.order)] = copy.deepcopy(root)
            self.order = []
            return

        for key, value in self.map.iteritems():
            if not value[0]:
                node = self.binarySearchTree(source, value[1])
                value[0] = True
                self.count += 1
                self.dfs(root, node)
                self.count -= 1
                value[0] = False
                source.left = None
                source.right = None


    def generateTrees(self, n):

        if n == 0:
            return []
        self.n = n
        self.generate_nodes()
        for key, value in self.map.iteritems():
            #pdb.set_trace()
            value[0] = True
            self.count += 1
            self.dfs(value[1], value[1])
            value[0] = False
            self.count -= 1
            value[1].left = None
            value[1].right = None

        print "***********", len(self.output)
        print self.output

a = Solution()
a.generateTrees(3)
