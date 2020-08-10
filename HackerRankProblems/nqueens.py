class Solution(object):

	def __init__(self):

		self.graph = None
		self.n = 0
		self.remove = {}

	def creategraph(self, n):
		self.n = n
		graph = [[True]*n for i in xrange(n)]
		print "graph:", graph
		return graph

	def is_not_under_attack(self, row, col):

		return self.graph[row][col]

	def place_queen(self, row, col):

		self.graph[row][col] = False
		self.remove[row] = [[row, col]]
		for i in xrange(self.n):
			if self.graph[row][i]:
				self.graph[row][i] = False
				self.remove[row].append([row, i])
			if self.graph[i][col]:
				self.graph[i][col] = False
				self.remove[row].append([i, col])
		i = row
		j = col
		while i >= 0 and j >=0 and j < self.n:
			if self.graph[i][j]:
				self.graph[i][j] = False
				self.remove[row].append([i, j])
			i -= 1
			j -= 1

		i, j = row, col
		while i < self.n and j >= 0 and j < self.n:
			if self.graph[i][j]:
				self.graph[i][j] = False
				self.remove[row].append([i, j])
			i += 1
			j += 1

		i, j = row, col
		while i >= 0 and j >= 0 and j < self.n:
			if self.graph[i][j]:
				self.graph[i][j] = False
				self.remove[row].append([i, j])
			i -= 1
			j += 1

		i, j = row, col
		while i < self.n and j >= 0 and j < self.n:
			if self.graph[i][j]:
				self.graph[i][j] = False
				self.remove[row].append([i, j])
			i += 1
			j -= 1

		print "After place:"
		print self.graph
		print "Remove index:", self.remove

	def remove_queen(self, row, col):

		array = self.remove[row]
		if array:
			for indexs in array:
				i, j = indexs[0], indexs[1]
				self.graph[i][j] = True
		'''
		self.graph[row][col] = True
		for i in xrange(self.n):
			self.graph[row][i] = True
			self.graph[i][col] = True
		i = row
		j = col
		while i >= 0 and j >=0 and j < self.n:
			self.graph[i][j] = True
			i -= 1
			j -= 1

		i, j = row, col
		while i < self.n and j >= 0 and j < self.n:
			self.graph[i][j] = True
			i += 1
			j += 1

		i, j = row, col
		while i >= 0 and j >= 0 and j < self.n:
			self.graph[i][j] = True
			i -= 1
			j += 1

		i, j = row, col
		while i < self.n and j >= 0 and j < self.n:
			self.graph[i][j] = True
			i += 1
			j -= 1
		'''
		print "After remove:"
		print self.graph


	def totalNQueens(self, n):

		self.graph = self.creategraph(n)
		import pdb
		#pdb.set_trace()
		return self.backtrack()

	def backtrack(self, row = 0, count = 0):
		for col in range(self.n):
		#iterate through columns at the curent row.
			if self.is_not_under_attack(row, col):
				# explore this partial candidate solution, and mark the attacking zone
				self.place_queen(row, col)
				if row + 1 == self.n:
					# we reach the bottom, i.e. we find a solution!
					count += 1
				else:
					# we move on to the next row
					count = self.backtrack(row + 1, count)
				# backtrack, i.e. remove the queen and remove the attacking zone.
				self.remove_queen(row, col)
		return count

a = Solution()
print a.totalNQueens(4)
