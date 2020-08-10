from collections import deque
class Solution(object):
	def updateMatrix(self, matrix):
		self.row, self.col = len(matrix), len(matrix[0])
		print "Row:", self.row, "Col:", self.col
		visited = {}
		#visited = {(i,j):False for i in xrange(row) for j in xrange(col)}
		result = []
		q = deque([])
		for i in xrange(self.row):
			temp = []
			for j in xrange(self.col):
				visited[(i,j)] = False
				#print "i:{}, j:{}".format(i,j)
				if matrix[i][j] == 0:
					q.append((i,j),)
					temp.append(matrix[i][j])
				else:
					temp.append(None)
			result.append(temp)
		print "visited:", visited
		print "q:", q
		print "result:", result
		return self.bfs(q, result, visited)

	def bfs(self, q, matrix, visited):

		while q:
			node = q.popleft()
			if not visited[node]:
				visited[node] = True
				source_i = node[0]
				source_j = node[1]
				for neighbour in self.get_neighbour(node):
					i = neighbour[0]
					j = neighbour[1]
					print "i:{}, j:{}".format(i,j)
					if matrix[i][j] is None or matrix[source_i][source_j] + 1 < matrix[i][j]:
						matrix[i][j] = matrix[source_i][source_j] + 1
						q.append((i,j),)
		print matrix
		return matrix

	def get_neighbour(self, index):
		i = index[0]
		j = index[1]
		result = []
		#up
		if i > 0:
			result.append((i-1, j),)
		#left
		if j > 0:
			result.append((i, j-1),)
		#right
		if j < self.col - 1:
			result.append((i, j+1),)
		#down
		if i < self.row - 1:
			result.append((i+1, j),)

		print "neigbours:", result
		return result

a = Solution()
print a.updateMatrix([[0,0,0],
 [0,1,0],
 [0,0,0]])
print a.updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]])
