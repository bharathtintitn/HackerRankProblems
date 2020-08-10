import pdb
from collections import defaultdict

class Solution(object):

    def wordBreak(self, s, wordDict):
        print "*********"
        self.hashmap = defaultdict(bool)
        for word in wordDict:
            self.hashmap[word] = True
        return self.bfs(s)

    def bfs(self, s):

        q = [0]
        visited = defaultdict(bool)
        print "map:", self.hashmap
        while q:
            print "q:", q
            start = q.pop(0)
            if start == len(s):
                return True
            if not visited[start]:
                end = start + 1
                while end <=len(s):
                    search = s[start:end]
                    print "search:", search
                    if self.hashmap[search]:
                        q.append(end)
                    visited[start] = True
                    end += 1

        return False

a = Solution()
print a.wordBreak('leetcode', ["leet", "code"])
print a.wordBreak('applepenapple', ["apple", "pen"])
print a.wordBreak('catsanddog', ["cats", "dog", "sand", "and", "cat"])
