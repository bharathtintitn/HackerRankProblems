import pdb
class Solution(object):

    def __init__(self):

        self.visited = set()

    def direction(self):

        for i,j in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
            yield [i, j]

    def turn(self, i, j, robot):
        if i == -1 and j == 1:
            robot.turnLeft()
        elif i == -1 and j == -1:
            robot.turnLeft()
        elif i == 1 and j == -1:
            robot.turnRight()
        else:
            robot.turnRight()

    def deturn(self, i, j, robot):
        if i == -1 and j == 1:
            robot.turnRight()
        elif i == -1 and j == -1:
            robot.turnRight()
        elif i == 1 and j == -1:
            robot.turnLeft()
        else:
            robot.turnLeft()

    def dfs(self, robot):

        if [self.row, self.col] not in self.visited:
            robot.clean()
            self.visited.add([self.row, self.col])
            for i, j in self.direction(self.row, self.col):
                self.turn(i, j, robot)
                if robot.move():
                    self.dfs(robot)
                    self.deturn(i, j, robot)
                else:
                    self.deturn(i, j, robot)

    def cleanRoom(self, robot):

        ilength = len(self.room)
        if ilength > 0:
            jlength = len(self.room[0])
        else:
            return

        print "ilen:", ilength, " jlen:", jlength


        return self.dfs(robot)

a = Solution()

