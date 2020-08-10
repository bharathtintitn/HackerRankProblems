class Solution(object):
    def verticalTraversal(self, root):
		def dfs(root, col, row, node):
			if not root:
				return node
			dfs(root.left, col-1, row+1, node)
			dfs(root.right, col+1, row+1, node)
			return node.append((col, row, node))
