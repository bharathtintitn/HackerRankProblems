class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pas = []
        for i in xrange(1, numRows+1):
            #print "i:", i
            temp = []
            for j in xrange(1, i+1):
                #print "j:", j
                #print self.pascal(i,j)
                temp.append(self.pascal(i, j, pas))
            pas.append(temp)
        return pas
    def pascal(self, i, j, pas):
        if j == 1 or j == i:
            return 1
        #print i, j, pas
        return pas[i-2][j-2] + pas[i-2][j-1]
        #return self.pascal(i-1, j-1, pas) + self.pascal(i-1, j, pas)


a = Solution()
print a.generate(3+1)[-1]
