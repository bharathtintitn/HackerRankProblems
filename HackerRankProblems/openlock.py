import collections
class Solution(object):
    def openLock(self, deadends, target):

        def neighbours(node):
            #print "node:", node
            for i in xrange(4):
                x = node[i]
                #print "x:", x, " i:", i
                s = int(x)
                for d in (-1, 1):
                    a = (s + d)%10
                    #print " a:", a, " s:", s
                    res = node[:i] + str(a) + node[i+1:]
                    yield res

        start = '0000'
        seen = {start}
        q = collections.deque([(start, 0)])
        dead = set(deadends)
        while q:
            node, depth = q.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbours(node):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth+1))

        return -1

a = Solution()
print a.openLock(["0201","0101","0102","1212","2002"], '0202')
