import pdb
import heapq
from collections import defaultdict

class Solution(object):

    def reorganizeString(self, s):
        result = ''
        if not s:
            return result
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1

        print freq
        h = []
        for i,j in freq.iteritems():
            h.append([-1*j, i])

        heapq.heapify(h)
        print h

        index = 0
        temp = []
        #pdb.set_trace()
        while len(result) <> len(s):
            print "heap:", h, result, temp
            if len(h) == 0:
                return ''
            node = heapq.heappop(h)
            if not result or result[index-1] <> node[1]:
                result += node[1]
                index += 1
                new = [node[0]+1, node[1]]
                if new[0] < 0:
                    heapq.heappush(h, new)
                if temp:
                    for n in temp:
                        if n[0] < 0:
                            heapq.heappush(h, n)
                    temp = []
            else:
                temp.append(node)

        return result



a = Solution()
print a.reorganizeString("aab")
print a.reorganizeString('aaab')

