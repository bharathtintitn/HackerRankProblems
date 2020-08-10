class Solution(object):
	def levelOrder(self, root):

		node = root
		result = []
		if not node:
			return result
		q = [node]
		result.append([node])
		while True:
			t = []
			while q:
				temp = q.pop()
				#children = temp.children
				for child in temp.children:
					t.append(child)
			if len(t) > 0:
				r = []
				for i in t:
					q.append(i)
					r.append(i.val)
				result.append(r)
			else:
				break
		print "result:", result
		return result

a = Solution()
a.levelOrder()
