class Node(object):

    def __init__(self):
        self.data = None
        self.child = {}

class Solution(object):

    def initial(self):
        self.root = Node()
    def removeSubfolders(self, folder):


        for item in folder:
            print "folder:", item
            if i == '/':
                continue
            for i in item:
                if self.root.child.get(i, False):
                    continue
                self.root.child[i] = {}

