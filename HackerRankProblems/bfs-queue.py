class Solution(object):
    def wallsAndGates(self, rooms):
		queue = []
		result = []
		visited = set()
		result = []
		if not rooms:
			return []
		m, n = len(rooms), len(rooms[0])
		def is_valid(a, b):

			if a >=0 and a < m and b >=0 and b < n:
				return True
			return False

		def bfs(a, b):
			print "Source:", a, b
			for i in xrange(m):
				for j in xrange(n):
					if rooms[i][j] == 0:
						queue.append((i,j),)
			print "Initial q:", queue

			while queue:

				node = queue.pop(0)
				a = node[0]
				b = node[1]
				for i,j in ((a-1, b), (a+1, b), (a, b-1), (a, b+1)):
					#print "i, j:", i, j
					if is_valid(i, j) and rooms[i][j] == 2147483647:
						rooms[i][j] = rooms[a][b] + 1
						queue.append((i,j),)
					#print "queue:", queue
		#queue.append((0,0),)
		bfs(0,0)

		print "Rooms:",
		print rooms

a = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1,2147483647, -1], [0, -1, 2147483647, 2147483647]]
a.wallsAndGates(rooms)
