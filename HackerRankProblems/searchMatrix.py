import pdb

class Solution(object):

    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        lo, hi = 0, len(matrix)*len(matrix[0]) - 1
        print lo, hi
        rlen = len(matrix[0])
        while lo <= hi:

            mid = (lo+hi)/2
            row = mid//rlen
            col = mid%rlen
            print "mid:{}, row:{}, col:{}".format(mid, row, col)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        print "No found"
        print "mid:{}, row:{}, col:{}".format(mid, row, col)
        return False

a = Solution()
print a.searchMatrix([[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]], 3)
print a.searchMatrix([
      [1,   3,  5,  7],
        [10, 11, 16, 20],
          [23, 30, 34, 50]
          ], 13)
