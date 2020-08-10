import pdb

from collections import defaultdict, Counter, deque

class Solution(object):

    def alienOrder(self, words):

        adjList = defaultdict(set)
        degree = Counter({c:0 for word in words for c in word})
        print "adjList:", adjList
        print "degree:", degree

        for first, second in zip(words, words[1:]):
            print "First:{}, second:{}".format(first, second)

            for c, d in zip(first, second):
                print "c:{}, d:{}".format(c,d)
                if c != d:
                    if d not in adjList[c]:
                        adjList[c].add(d)
                        degree[d] += 1
                    break
                else:
                    if len(d) < len(c): return ""

        print "degree:", degree
        print "list:", adjList
        q = deque([i for i in degree if degree[i] == 0])
        output = []

        while q:

            node = q.popleft()
            output.append(node)
            for nei in adjList[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)

        if len(output) < len(degree):
            return ""
        return output

a = Solution()
print a.alienOrder([
      "wrt",
        "wrf",
          "er",
            "ett",
              "rftt"
              ])

print a.alienOrder([
      "z",
        "x",
          "z"
          ])
