import pdb
import copy
from collections import deque, defaultdict

class Solution(object):

    def lastStoneWeightII(self, stones):

        self.taken = [False]*len(stones)
        print "Taken:", self.taken

        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]
        stones = sorted(stones)
        print "Stones:", stones
        self.min_remin = float('inf')
        self.visited = defaultdict(tuple)
        self.backtrack(stones)
        print "min:", self.min_remin
        return self.min_remin

    def backtrack(self, stones):

        if len(stones) == 1:
            print "**********", stones, self.min_remin, sum(stones)
            if self.min_remin > sum(stones):
                self.min_remin = sum(stones)
                print "===>min:", self.min_remin
            return stones[0]
        key = tuple(stones)
        if self.visited[key]:
            return self.visited[key]
        stone = stones.pop()
        print "Stone:", stone
        array = copy.deepcopy(stones)
        array_c = copy.deepcopy(array)
        print array, array_c, stones
        #pdb.set_trace()
        for i in range(len(array)):
            next_stone = array[i]
            array_c.pop(i)
            print array_c
            add = abs(next_stone-stone)
            print "add:", add
            array_c.append(add)
            array_p = sorted(array_c)
            reminder = self.backtrack(copy.deepcopy(array_p))
            array_c = copy.deepcopy(array)
            if self.visited[key]:
                if self.visited[key] > reminder:
                    self.visited[key] = reminder
            else:
                self.visited[key] = reminder


            if reminder == 0 or self.min_remin == 0:
                pdb.set_trace()
                self.min_remin = 0
                print "$$$$$$$=>min:", self.min_remin

                return 0




a = Solution()
a.lastStoneWeightII([2,7,4,1,8,1])
