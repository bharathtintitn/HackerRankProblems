import pdb

class Node(object):

    def __init__(self):

        self.t = {}
        self.word = ""

    def __str__(self):
        return "word: " + self.word + " t:" +  str(self.t)

    def __repr__(self):
        return "word: " + self.word + " t:" + str(self.t)

class Solution(object):
    def __init__(self):

        self.tries = Node()

    def addWord(self, word):

        tries = self.tries
        pdb.set_trace()
        for i in word:
            if tries.t.get(i, False):
                tries = tries.t[i]
            else:
                tries.t[i] = Node()
                prev = tries
                tries = tries.t[i]
        tries.word = word
        print "Tries:", self.tries

    def has_root(self, word):

        tries = self.tries
        add = ""
        for i in word:
            if tries.t.get(i, False):
                if tries.word:
                    add = tries.word + " "
                    return add
                add += i
                tries = tries.t[i]
            else:
                if tries.word:
                    return word + " "
                return word + " "
        return word + " "

    def replaceWords(self, dick, sentence):

        array = sentence.split()
        print "array:", array
        if len(array) == 0:
           return ""

        for word in dick:
            self.addWord(word)

        sent = ""
        pdb.set_trace()
        for w in array:
            add = self.has_root(w)
            sent += add
        print "Sent:", sent
        return sent.strip()


a = Solution()
print a.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
