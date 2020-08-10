import pdb

class Node(object):

    def __init__(self):
        self.ch = {}
        self.v = 0

    def __str__(self):
        return str(self.ch) + " " + str(self.v)

class AutocompleteSystem(object):

    def __init__(self, sentences, times):

        self.tries = Node()
        self.update(sentences, times)
        self.string = ""
        self.search = None

    def update(self, sentences, times):

        #pdb.set_trace()
        for i, sen in enumerate(sentences):
            node = self.tries
            #print "node:", node
            for c in sen:
                if node.ch.get(c, False):
                   node = node.ch[c]
                else:
                   n = Node()
                   node.ch[c] = n
                   node = n
            node.v += times[i]
            #print "End node:", node


        #print "tries:", str(self.tries)
        self.string = ""
        self.search = None
        #self.display()

    def search_string(self, node, string, index):

        for i in xrange(index, len(string)):
            char = string[i]
            if node.ch.get(char, False):
                node = node.ch[char]
            else:
                return None
        return node

    def get_guess(self, node, result, string):

        vertex = node
        for ch, n in vertex.ch.iteritems():
            strin = string + ch
            v, s = self.get_guess(n, result, strin)
            if v <> None and v <> 0:
                result.append((v, s))
            strin = string
        value = vertex.v, string

        if vertex == None:
            return None, None
        return vertex.v, string

    def display(self):

        node = self.tries
        print node
        q = []
        q.append((node.ch, node, node.v))
        while q:
            c, v, val = q.pop(0)
            temp = []
            for i, j in v.ch.iteritems():
                temp.append((i, j, v.v))
            #print "temp:", temp, " value:", v.v, c
            q.extend(temp)

    def input(self, c):

        if c == '#' and len(self.string) > 0:
            #print "string adding:", self.string
            self.update([self.string], [1])
        if c <> '#':
            return self.go(c)

    def go(self, string):

        if not self.search:
            node = self.tries
            self.index = 0
        else:
            node = self.search
            self.index = len(self.string)-1
        self.string += string
        #print "string:", self.string
        #print "index:", self.index
        #pdb.set_trace()
        vertex = self.search_string(node, self.string, self.index)
        self.search = vertex
        #pdb.set_trace()
        result = []
        if vertex:
            self.get_guess(vertex, result, "")
            #print "result:", result
            #return sorted(result)
            return self.final(result)
        else:
            return result

    def final(self, result):

        res = []
        #result = sorted(result, key=lambda tup: tup[0])
        result.sort(key=lambda tup: tup[0], reverse=True)
        #print "Result:", result
        for i, j in result:
            res.append(self.string + j)
            if len(res) == 3:
                return res
        return res


a = AutocompleteSystem(["i love you", "island","ronman", "i love leetcode"], [5,3,2,2])
#pdb.set_trace()
print a.input('')
print a.input('i')
print a.input(' ')
print a.input('a')
print a.input('#')
print a.input('')
print a.input('i')
print a.input(' ')
#pdb.set_trace()
print a.input('a')
