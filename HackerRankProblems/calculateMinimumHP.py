import pdb
from collections import defaultdict

class Solution(object):

    def __init__(self):

        self.m = 0
        self.n = 0
        self.visited = defaultdict(bool)
        self.min_power = 0

    def isValid(self, row, col):

        if row >= 0 and row < self.m and col >=0 and col < self.n:
            return True
        return False

    def calculateMinimumHP(self, dungeon):

        self.m = len(dungeon)
        if self.m > 0:
            self.n = len(dungeon[0])
        else:
            return 1
        self.graph = dungeon
        source = (0,0)
        self.dfs(source, 1, [0])
        print "Power:", self.min_power
        return self.min_power

    def dfs(self, source, power, power_add):

        if sum(power_add) > self.min_power:
            self.min_power = sum(power_add)

        if not self.visited[source]:
            self.visited[source] = True
            row, col = source[0], source[1]
            health = self.graph[row][col]
            if (power + health) <= 0:
                add = (abs(health) - power + 1)
                power += (health + add)
                power_add.append(add)
            else:
                power += health
            for row, col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neig = (row, col)
                if self.isValid(row, col) and not self.visited[neig]:
                    self.dfs(neig, power, power_add)

a = Solution()
assert a.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]), 7


