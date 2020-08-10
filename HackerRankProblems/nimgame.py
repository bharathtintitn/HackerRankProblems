class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if 1 <= n <=3:
            return True
        
        for i in xrange(1,4):
            opp = n - i
            if 1 <= opp <= 3:
                return False
            for j in xrange(1,4):
                ret = self.canWinNim(opp-j)
                if ret:
                    return True
            
        return False

import pdb
pdb.set_trace()
a = Solution()
a.canWinNim(8)
print a
