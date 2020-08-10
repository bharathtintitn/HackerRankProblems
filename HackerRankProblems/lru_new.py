import pdb
from collections import defaultdict

class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

	def __init__(self, capacity):
		self.cap = capacity
		self.count = 0
		self.hashmap = defaultdict(bool)
		self.head = Node(None)
		self.tail = Node(None)
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key):
		print "Get hash:", self.hashmap, " key:", key
		if self.hashmap[key]:
			node = self.hashmap[key]
			self.update(node, key)
			return node.val
		return -1

	def put(self, key, value):

		if self.hashmap[key]:
			node = self.hashmap[key]
			node.val = value
			self.update(node, key)
		else:
			node = Node(value)
			self.hashmap[key] = node
			if self.count >= self.cap:
				ret = self.delete()
			else:
				self.count += 1
			self.update(node, key)

	def update(self, node, key):

		prev = node.prev
		nex = node.next
		if prev:
			prev.next = nex
		if nex:
			nex.prev = prev

		node.prev = None
		node.next = None

		curr = self.head.next
		self.head.next = node
		node.prev = self.head
		node.next = curr
		curr.prev = node

	def delete(self):

		node = self.tail.prev
		print "deleting:", node.val
		prev = node.prev
		node.next = None
		node.prev = None
		prev.next = self.tail
		self.tail.prev = prev
