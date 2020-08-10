import pdb

class Solution(object):

    def __init__(self):

        self.dp = {}

    def getRow(self, rowIndex):

        if rowIndex == 0:
            return []
        rowIndex += 1
        def recurr(rowIndex):

            if rowIndex == 0:
                return []
            if rowIndex == 1:
                return [1]
            elif rowIndex == 2:
                return [1,1]
            else:
                if self.dp.get(rowIndex, False):
                    return self.dp[rowIndex]
                else:
                    ret = recurr(rowIndex-1)
                    self.dp[rowIndex-1] = ret
                    temp = [1]
                    for i in xrange(1, rowIndex-1):
                        temp.append(ret[i]+ret[i-1])
                    temp.append(1)
                    self.dp[rowIndex] = temp
                return temp

        r = recurr(rowIndex)
        print r
        return r

a = Solution()
a.getRow(3)
a.getRow(4)
a.getRow(5)

