import pdb

class Solution(object):

    def __init__(self):

        self.map = {chr(i):[] for i in xrange(97, 97+26)}
        print "map:", self.map

    def findWords(self, board, words):

        def isValid(one, two):
            if (one >= 0 and one < len(board)) and \
                    (two >= 0 and two < len(board[0])):
                return True
            return False

        visited = set()
        def dfs(word, indexI, indexJ, index):
            if index == len(word):
                return True
            if not isValid(indexI, indexJ):
                return False
            if (indexI, indexJ) in visited:
                return False
            visited.add((indexI, indexJ),)
            print "word:", word, "visited:", visited
            for i,j in ((0,-1), (0,1), (1, 0),(-1,0)):
                nextI, nextJ = indexI+i, indexJ+j
                if isValid(nextI, nextJ) and ((nextI, nextJ) not in visited):
                    if word[index] == board[nextI][nextJ]:
                        if dfs(word, nextI, nextJ, index+1):
                            return True

            return False


        if not words:
            return []
        if not board:
            return []
        if len(board[0]) == 0:
            return []

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                ch = board[i][j]
                self.map[ch].append([i,j])
        print "Map:", self.map
        present = []
        for word in words:
            vertex = self.map[word[0]]
            print "c:", word[0], "vertex:", vertex
            for node in vertex:
                pdb.set_trace()
                visited = set()
                if dfs(word, node[0], node[1], 1):
                    present.append(word)
                    break
        print "present:", present
        return present

a = Solution()
a.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain"])
a = Solution()
a.findWords([["a","a"]], ["aaa"])
