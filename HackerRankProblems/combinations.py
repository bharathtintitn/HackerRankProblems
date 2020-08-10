import pdb
import copy

class Solution(object):

    def combine(self, n, k):

        hashmap = {i: False for i in xrange(1, n+1)}
        print "map:", hashmap
        result = []

        def dfs(res, index):

            if len(res) == k:
                print res
                result.append(copy.deepcopy(res))
                return

            #for key, value in hashmap.iteritems():
            #    if not value:
            #        res.append(key)
            #        hashmap[key] = True
            #        dfs(res)
            #        res.pop()
            #        hashmap[key] = False

            for i in xrange(index, n+1):
                #pdb.set_trace()
                res.append(i)
                dfs(res, i+1)
                res.pop()

        if n == 0 or k == 0:
            return []
        dfs([], 1)
        print result
        return result

a = Solution()
a.combine(4, 2)
