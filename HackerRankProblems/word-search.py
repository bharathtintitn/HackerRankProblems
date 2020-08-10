from collections import defaultdict
import pdb
class Solution(object):

	def indexing(self, board):
		self.location = defaultdict(list)
		for i, row in enumerate(board):
			for j, letter in enumerate(row):
				self.location[letter].append((i,j),)

		print "Locations: ", self.location

	def find_letters(self, letter, i, j):
		loc = []
		#upper boundary
		if i != 0 and letter == self.board[i-1][j]:
			loc.append([i-1, j])

		if j != 0 and letter == self.board[i][j-1]:
			loc.append([i, j-1])

		if i != self.iboundary and letter == self.board[i+1][j]:
			loc.append([i+1, j])

		if j != self.jboundary and letter == self.board[i][j+1]:
			loc.append([i, j+1])

		return loc

	def is_present(self, word, index, visited, i, j):

		if index >= len(word):
			return False

		letter = word[index]
		print "Next letter to search: ", letter
		loc = self.find_letters(letter, i, j)
		for l in loc:
			if not visited[l[0], l[1]]:
				visited[l[0],l[1]] = True
				if index == len(word) - 1:
					return True
				if self.is_present(word, index+1, visited, l[0], l[1]):
					return True
				visited[l[0], l[1]] = False
		return False

	def find_word(self, word):
		if word:
			start = word[0]
			index = 1
			row = self.location[start]
			visited = defaultdict(bool)
			if index == len(word):
				if len(row) > 0:
					return True
				else:
					return False
			for i,j in row:
				visited[i,j] = True
				if self.is_present(word, index, visited, i, j):
					return True
				visited[i,j] = False
		return False

	def findWords(self, board, words):
		self.board = board
		self.indexing(board)
		self.iboundary = len(board) - 1
		self.jboundary = len(board[0]) - 1
		result = []
		#print 'indexing: ', self.location
		for word in words:
			#pdb.set_trace()
			if self.find_word(word):
				result.append(word)
		print "Final result: ", result
		return result

a = Solution()
a.findWords([["a"]], ['a'])
a.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])
