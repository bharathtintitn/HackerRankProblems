import pdb

class Solution(object):

    def numWaterBottles(self, nb, ne):
        print "*******"
        if ne > nb:
            print nb
            return nb
        if ne == nb:
            print nb+1
            return nb+1

        res = nb
        while nb >= ne:
            res += (nb/ne)
            nb = (nb/ne) + (nb%ne)
        print res
        return res

a = Solution()
a.numWaterBottles(9, 3)
a.numWaterBottles(15, 4)
a.numWaterBottles(5, 5)
a.numWaterBottles(2, 3)

