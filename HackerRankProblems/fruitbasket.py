class Solution(object):
	def totalFruit(self, tree):
		print '##################'
		def get_index(b, j, i):
			index = j-1
			while index >= i:
				if b == tree[index]:
					index -= 1
				else:
					return index + 1
			return index+1

		basket1 = None
		basket2 = None

		i = 0
		j = 0

		length = len(tree) - 1
		print "Length:", length

		if length < 0:
			return 0
		if length == 0:
			return 1
		max_length = 0
		while i <= j and j <= length:
			fruit = tree[j]
			if basket1 is None:
				basket1 = fruit
				max_length = 1
			elif basket2 is None and fruit <> basket1:
				basket2 = fruit
				max_length += 1
			else:
				if tree[j] == basket1 or tree[j] == basket2:
					max_length = max(max_length, j-i+1)
				else:
					i = get_index(tree[j-1], j, i)
					basket1 = tree[j-1]
					basket2 = tree[j]
					print "Index got: ", i, " basket1:", basket1, " basket2:", basket2, " j:", j , " max_length:", max_length
			j += 1
			print "Basket1:", basket1, " Basket2:", basket2, " j:", j , " i:", i, " max:", max_length
		print "max_length:", max_length, " tree:", tree
		return max_length
a = Solution()
a.totalFruit([1,2,1])
a.totalFruit([1,2,3,2,2])
a.totalFruit([0,1,2,2])
a.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
a.totalFruit([3, 3, 3, 1, 4])
