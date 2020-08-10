
class Node(object):

    def __init__(self, start, end):

        self.start = start
        self.end = end
        self.total = None
        self.left = None
        self.right = None

    def display(self, root):

        if root:
            self.display(root.left)
            print root.total,
            self.display(root.right)

class NumArray(object):

    def __init__(self, nums):

        def createTree(nums, l, r):

            if l > r:
                return None

            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node

            mid = (l + r)//2
            #print mid
            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)

            root.total = root.left.total + root.right.total

            return root

        self.root = createTree(nums, 0, len(nums)-1)
        self.root.display(self.root)

    def update(self, i, val):

        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return
            mid = (root.start + root.end)//2
            print "mid:", mid
            if mid >= i:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total

        return updateVal(self.root, i, val)

    def sumRange(self, i, j):

        def rangeSum(root, i, j):

            if root.start == root.end:
                return root.total

            mid = (root.start + root.end) //2
            print "sum mid:", mid
            if j <= mid:
                return rangeSum(root.right, i, j)

            elif i >= mid+1:
                return rangeSum(root.left, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)





a = NumArray([1,3,5])
a.update(1,2)
a.root.display(a.root)
a.update(0,7)
a.root.display(a.root)
print a.sumRange(0,2)
