class Tries(object):

	def __init__(self, value=0):
		self.vertex = {}
		self.value = value

	def __str__(self):
		return "vertex:" + str(self.vertex)+ " value:" + str(self.value)

class MapSum(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.tries = Tries()

	def insert(self, key, val):
		"""
		:type key: str
		:type val: int
		:rtype: None
		"""
		node = self.tries
		for i in key:
			if node.vertex.get(i, False):
				node = node.vertex[i]
			else:
				node.vertex[i] = Tries()
				node = node.vertex[i]
		node.value = val
		print "Tries:", self.tries
		#self.display()

	def display(self):

		node = self.tries
		q = [node]
		while q:
			node = q.pop(0)
			for key, value in node.vertex.iteritems():
				print "key: ", key, " value:", value
				q.append(value)

	def sum(self, prefix):
		"""
		:type prefix: str
		:rtype: int
		"""
		total = 0
		node = self.tries
		for i in prefix:
			if node.vertex.get(i, False):
				node = node.vertex[i]
			else:
				return 0
		total = self.get_sum(node)
		print "total:", total
		return total

	def get_sum(self, node):
		total = 0
		queue = [node]
		while len(queue) > 0:
			node = queue.pop(0)
			total += node.value
			for key, vertex in node.vertex.iteritems():
				queue.append(vertex)
				#total += vertex.value
		print "After all:", total
		return total

obj = MapSum()
obj.insert("apple", 3)
import pdb
pdb.set_trace()
param_2 = obj.sum('ap')
print param_2
obj.insert("app", 2)
print obj.sum("ap")
