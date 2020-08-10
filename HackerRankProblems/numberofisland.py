class Solution(object):
    def numIslands(self, grid):
		i_length = len(grid)-1
		j_length = len(grid[0])-1
		if i_length == 0:
			return 0
		def is_island(node):
			i, j = node[0], node[1]
			count = 0
			print "i, j:", i,j
			for neighbour in ((i-1,j),(i,j-1),(i,j+1),(i+1,j)):
				if neighbour[0] < 0:
					count += 1
				if neighbour[0] > i_length:
					count += 1
				if neighbour[1] < 0:
					count += 1
				if neighbour[1] > j_length:
					count += 1

				if neighbour[0] >= 0 and neighbour[0] <= i_length and neighbour[1] >= 0 and neighbour[1] <= j_length:
					print "neg:", neighbour
					if grid[neighbour[0]][neighbour[1]] == 0:
						count += 1
			print "Node:", node, " island:", count
			if count < 4 and count > 0:
				return True
			return False

		island = []
		count = 0
		for i in xrange(len(grid)):
			for j in xrange(len(grid[0])):
				if grid[i][j] == 1:
					island.append((i,j),)
		print "Number of land:", len(island)
		for node in island:
			if is_island(node):
				count += 1
		print "total island:", count
		return count


a = Solution()
a.numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
