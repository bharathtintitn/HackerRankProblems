import pdb
class Solution(object):

    def __init__(self):

        self.visited = set()
        self.turned = {}
        self.direction = 'Front'

    def get_direction(self, robot):

        if self.direction == 'Front':
            robot.turnLeft()
            return 'Left'
        elif self.direction == 'Left':
            robot.turnLeft()
            return 'Back'
        elif self.direction == 'Back':
            robot.turnLeft()
            return 'Right'
        elif self.direction == 'Right':
            robot.turnLeft()
            return 'Front'

    def turn_direction(self, new_direction):

        if new_direction == 'Front':
            return 'Left'
        elif new_direction == 'Left':
            return 'Back'
        elif new_direction == 'Back':
            return 'Right'
        elif new_direction == 'Right':
            return 'Front'

    def dfs(self, robot):

        if (robot.row, robot.col) not in self.visited:
            robot.clean()
            if not self.turned.get((robot.row, robot.col), False):
                self.turned[(robot.row, robot.col)] = set()
            print "****************"
            print "row:", robot.row, " col:", robot.col, " turned:", self.turned
            while len(self.turned[(robot.row, robot.col)]) < 4:
                print " Direction:", self.direction, " turned:", self.turned
                if self.direction not in self.turned[(robot.row, robot.col)]:
                    if robot.move():
                        self.dfs(robot)
                self.turned[(robot.row, robot.col)].add(self.direction)
                self.direction = self.get_direction(robot)
                #self.turn_direction(new_direction)
                #self.direction = self.get_direction()

            self.visited.add((robot.row, robot.col))

    def cleanRoom(self, robot):

        ilength = len(robot.room)
        if ilength > 0:
            jlength = len(robot.room[0])
        else:
            return

        print "ilen:", ilength, " jlen:", jlength


        return self.dfs(robot)

a = Solution()

