import pdb
import copy

from collections import defaultdict

class Node(object):

    def __init__(self):
        self.vertex = {}
        self.ch = ''
        self.isEnd = False

class Solution(object):

    def __init__(self):
        self.tries = Node()
        self.taken = defaultdict(bool)
        self.final = []
        self.present = {}

    def createTries(self, words):

        for word in words:
            node = self.tries
            for c in word:
                if node.vertex.get(c, False):
                    node = node.vertex[c]
                else:
                    n = Node()
                    node.vertex[c] = n
                    node = n
            node.isEnd = True

    def dfs(self, string, node, result):

        if len(string) == self.length:
            result.append(string)

        for key, value in node.vertex.iteritems():
            word = self.dfs(string+key, value, result)
            string = string

    def getWord(self, character):

        if len(character) == self.length:
            return [character]
        node = self.tries
        result = []
        isWord = False
        for c in character:
            if node.vertex.get(c, False):
                node = node.vertex[c]
            else:
                break
            isWord = True
        res = []
        if isWord:
            for key, values in node.vertex.iteritems():
                word = self.dfs(character+key, values, res)
        print "returns better string:", res
        return res

    def util(self, string, result, index):

        if len(result) == len(result[0]):
            if not self.present.get(tuple(result), False):
                self.final.append(copy.deepcopy(result))
            print "final", self.final
            return
        ret = self.getWord(string)
        for w in ret:
                    #if self.validate(w):
                    #if not self.taken[w]:
                    if w in self.words:
                        result.append(w)
                        self.taken[w] = True
                        search = self.get_search(result)
                        self.util(search, result, index+1)
                        self.taken[w] = False
                        result.pop()

    def get_search(self, result):
        string = ''
        index = len(result)
        for i, word in enumerate(result):
            if index < self.length:
                print "index:", index, " length:", self.length, " string:", string
                string += word[index]
        return string

    def go(self, words):

        result = []
        index = 0
        self.words = words
        for word in words:
            self.taken[word] = True
            result.append(word)
            self.length = len(word)
            #if self.length > 1:
            string = self.get_search(result)
            next_word = self.util(string, result, index)
            self.taken[word] = False
            result.pop()

    def wordSquares(self, words):

        self.createTries(words)
        #pdb.set_trace()
        self.go(words)
        print "final:", self.final
        return self.final

a = Solution()
a.wordSquares(["area","lead","wall","lady","ball"])
a = Solution()
a.wordSquares(["abat","baba","atan","atal"])
