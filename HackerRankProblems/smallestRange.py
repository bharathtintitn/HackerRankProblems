import pdb
from collections import defaultdict
import heapq as heap

class Solution(object):

    def smallestRange(self, nums):

        def retMax(array):
            if not array:
                return 0, 0
            ret = []
            for i,j in array:
                ret.append(i)
            return min(ret), max(ret)

        a = len(nums)
        h = []
        ids = {}
        counter = {}
        for i in xrange(a):
            ids[i] = nums[i]
            counter[i] = 0

        print ids
        print counter
        ranges = []
        for key, value in counter.iteritems():
            if value < len(ids[key]):
                h.append([ids[key][value], key])
                counter[key] += 1
            else:
                return ranges

        if not ranges:
            heap.heapify(h)
            a, b = retMax(h)
            ranges = [a,b]
            pdb.set_trace()
            while True:
                pdb.set_trace()
                item = heap.heappop(h)
                print "item:", item
                key = item[1]
                row = ids[key]
                index = counter[key]
                print "key:{}, row:{}, index;{}".format(key, row, index)
                if index < len(row):
                    value = row[index]
                    counter[key] += 1
                else:
                    break

                heap.heappush(h, [value, key])
                c, d = retMax(h)
                print "ranges:", ranges
                if (d-c) < (ranges[1]-ranges[0]) or \
                    ((ranges[1]-ranges[0]) == (d-c) and c < ranges[0]):
                        ranges = [c, d]
                print "range:", ranges
        print "Final:", ranges
        return ranges


a = Solution()
a.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
