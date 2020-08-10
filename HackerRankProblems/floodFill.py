import pdb
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.isVisited = {}
        self.vertical = len(image)
        if self.vertical == 0:
            return image
        self.hori = len(image[0])
        self.image = image
        oldColor = self.image[sr][sc]
        self.dfs(sr, sc, newColor, oldColor)
        print self.image
        return self.image
    
    def isValid(self, sr, sc):
        
        if 0 <= sr < self.self.vertical and 0 <= sc < self.hori:
            return True
        return False
        
        
    def dfs(self, sr, sc, newColor, oldColor):
        
        if not self.isValid(sr, sc):
            return
        if self.isVisited.get((sr, sc), False):
            return
        
        if self.image[sr][sc] == oldColor:
            self.image[sr][sc] = newColor
        else:
            return
            
        self.isVisited[(sr, sc)] = True
        for i,j in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_sr, new_sc = sr + i, sc + j
            self.dfs(new_sr, new_sc, newColor, oldColor)
            

a = Solution()
pdb.set_trace()
print a.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
