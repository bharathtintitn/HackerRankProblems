import pdb

class Solution(object):

    def solveSudoku(self, board):

        self.board = board
        self.queue = []
        self.getAllIndex()
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.gosudoku(0)
        print "Final:", self.board


    def getAllIndex(self):

        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j] == '.':
                    self.queue.append((i,j))

        print "queue:", self.queue


    def isValidNumber(self, index, number):

        row, col = index[0], index[1]
        for i in xrange(9):
            if self.board[row][i] == number or self.board[i][col] == number:
                return False

        r1, r2 = None, None
        if 0 <= index[0] <= 2:
            r1, r2 = 0, 3
        elif 3 <= index[0] <= 5:
            r1, r2 = 3, 6
        else:
            r1, r2 = 6, 9

        c1, c2 = None, None
        if 0 <= index[1] <= 2:
            c1, c2 = 0, 3
        elif 3 <= index[1] <= 5:
            c1, c2 = 3, 6
        else:
            c1, c2 = 6, 9

        for i in xrange(r1, r2):
            for j in xrange(c1, c2):
                if self.board[i][j] == number:
                    return False
        return True

    def gosudoku(self, index):

        if index > len(self.queue)-1:
            return True

        pos = self.queue[index]
        print "pos:", pos

        for num in self.numbers:
            if self.isValidNumber(pos, num):
                i, j = pos[0], pos[1]
                self.board[i][j] = num
                ret = self.gosudoku(index+1)
                if ret:
                    return ret
                self.board[i][j] = "."
        return False


a = Solution()
a.solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ])
