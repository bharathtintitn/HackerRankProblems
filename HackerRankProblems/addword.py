import pdb
class Node(object):

    def __init__(self):
        self.ch = {}
        self.end = ''

    def __str__(self):
        return str(self.ch)

class WordDictionary(object):

    def __init__(self):
        self.tries = Node()

    def addWord(self, string):

        node = self.tries
        #pdb.set_trace()
        for s in string:
            if node.ch.get(s, False):
                node = node.ch[s]
                #node = n
            else:
                node.ch[s] = Node()
                node = node.ch[s]
        node.end = 'end'
        print "node:", self.tries

    def dfs(self, root, index, string):

        if index >= len(string):
            print "ch:", root.ch, ' ', root.end
            if root.end == 'end':
                return True
            return False
        c = string[index]
        if c == '.':
            for key, value in root.ch.iteritems():
                ret = self.dfs(value, index+1, string)
                if ret:
                    return True
        elif root.ch.get(c, False):
            node = root.ch[c]
            ret = self.dfs(node, index+1, string)
            return ret
        return False

    def search(self, string):

        node = self.tries
        if len(string) == 0:
            return True
        index = 0
        #pdb.set_trace()
        ret = self.dfs(node, index, string)
        print "ret:", ret
        return ret


a = WordDictionary()
a.addWord("bad")
a.addWord("dad")
a.addWord("mad")
a.search("pad")
a.search("bad")
a.search(".ad")
a.search("b..")
