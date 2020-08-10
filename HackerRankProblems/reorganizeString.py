import pdb
import heapq as heap
from collections import defaultdict

class Solution(object):

    def reorganizeString(self, s):
        print "**********"
        length = len(s)
        if length == 0:
            return ""
        if length == 1:
            return s
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        print("Freq:", freq)

        #create heap 
        h = []
        for key, value in freq.items():
            h.append([-1*value, key])
        heap.heapify(h)
        print("Heap:", h)

        max_val = h[0][0]*-1
        print('max_val;', max_val)
        if length%2 == 0 and max_val > (length/2):
            return ''
        if length%2 != 0 and max_val > ((length/2) + 1):
            return ''

        result = ''
        dh = []
        while h:
            #pdb.set_trace()
            ch = heap.heappop(h)
            result += ch[1]
            if (ch[0]*(-1)) - 1 == 0:
                ch = []
            else:
                ch[0] = ((ch[0]*(-1)) - 1) * -1
            if len(dh) > 0:
                heap.heappush(h, dh)
            print("heap:", h)
            dh = ch
            ch = []
        print(result)
        return result



a = Solution()
print a.reorganizeString('aab')
print a.reorganizeString('aaab')
print a.reorganizeString('aaacb')






