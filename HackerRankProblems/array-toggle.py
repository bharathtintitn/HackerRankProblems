class Solution(object):

    def findDiagonalOrder(self, matrix):

        direction = True
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            n = 0

        result = []
        i = 0
        j = 0
        print "M:", m, " N:", n
        while i < m and j < n:
            result.append(matrix[i][j])
            if direction:
                if i == 0:
                    direction = False
                    if j == n-1:
                        i += 1
                    else:
                        j += 1
                else:
                    i -= 1
                    j += 1
                print "Direction Next: ", direction, " i:", i, " j:", j
            else:
                if j == 0 or i == m-1:
                    direction = True
                    if i == m-1:
                        j += 1
                    else:
                        i += 1
                else:
                    i += 1
                    j -= 1
                print "Direction next: ", direction, " i:", i, " j:", j
        print "Result:", result
        return result

a = Solution()
import pdb
pdb.set_trace()
a.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
a.findDiagonalOrder([])
a.findDiagonalOrder([[]])

