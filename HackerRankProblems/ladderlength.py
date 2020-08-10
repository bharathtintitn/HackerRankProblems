import pdb
from collections import defaultdict, deque

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        print '*************'

        q = deque([])
        L = len(beginWord)
        starWords = defaultdict(list)
        for word in wordList:
            for i in xrange(L):
                w = word[:i] + '*' + word[i+1:]
                starWords[w].append(word)
        print starWords

        q.append((beginWord, 1),)
        visited = defaultdict(bool)
        visited[beginWord] = True
        while q:

            node, level = q.popleft()
            print "1:",node, level, q

            for i in xrange(L):

                intermi = node[:i]+'*'+node[i+1:]
                print "inter:", intermi
                for w in starWords[intermi]:
                    print "w;", w, visited
                    if w == endWord:
                        return level + 1
                    #pdb.set_trace()
                    if not visited[w]:
                        "adding:", w
                        visited[w] = True
                        q.append((w, level+1))

        return 0


a = Solution()
print a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
