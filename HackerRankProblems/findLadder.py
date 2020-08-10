import pdb
import copy
from collections import defaultdict, Counter, deque

class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        wordL = len(beginWord)
        hashmap = defaultdict(list)
        for word in wordList:
            for i in xrange(wordL):
                w = word[:i] + '*' + word[i+1:]
                if w not in hashmap[w]:
                    hashmap[w].append(word)

        print "Map:", hashmap
        result = []
        q = deque([[beginWord, [beginWord]]])
        visited = defaultdict(bool)
        while q:

            node, array  = q.popleft()
            print node, array
            visited[node] = True
            #adding = copy.deepcopy(array)
            for i in xrange(wordL):
                w = node[:i] + '*' + node[i+1:]
                print "going for:", w, " array:", array
                for word in hashmap[w]:
                    if word == endWord:
                        adding = copy.deepcopy(array)
                        adding.append(word)
                        if not result:
                            result.append(adding)
                        else:
                            if len(result[0]) > len(adding):
                                result = [adding]
                            elif len(result[0]) == len(adding):
                                result.append(adding)
                    print "1: q:", q
                    #pdb.set_trace()
                    if not visited[word]:
                        new = copy.deepcopy(array)
                        new.append(word)
                        print "New:", new, q
                        q.append([word, new])
        print "result:", result
        return result
a = Solution()
a.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
