class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if not curr.get(c, False):
                curr[c] = {}
            curr = curr[c]
                
        print "word: ", self.root

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        curr = self.root
        print "Search:", word, " root:", self.root
        for c in word:
            print 'charac:', c
            if curr.get(c, False):
                curr = curr[c]
            else:
                return False
        return True
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        self.search(prefix)

obj = Trie()
import pdb
pdb.set_trace()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.startsWith(prefix)
