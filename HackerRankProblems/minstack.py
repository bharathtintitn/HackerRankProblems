class MinStack(object):

	def __init__(self):
		self.stack = []
		self.minstack = float('-inf')
		self.minarray = []
		self.tops = -1

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		if self.tops == -1:
			self.stack.append(x)
			self.minarray.append(x)
			self.tops += 1
			return
		if x > self.minarray[self.tops]:
			self.minarray.append(self.minarray[self.tops])
		else:
			self.minarray.append(x)
		self.stack.append(x)
		self.tops += 1

	def pop(self):
		"""
		:rtype: None
		"""
		if self.tops == -1:
			return
		item = self.stack[self.tops]
		item = self.stack.pop()
		minarr = self.minarray.pop()
		self.tops -= 1
		print "item:", item, " min:", minarr

	def top(self):
		"""
		:rtype: int
		"""
		if self.tops == -1:
			return -1
		print "stack:", self.stack, " top:", self.tops
		return self.stack[self.tops]

	def getMin(self):
		"""
		:rtype: int
		"""
		if self.tops == -1:
			return -1
		return self.minarray[self.tops]

a = MinStack()
minStack = MinStack();
print minStack.push(-2);
print minStack.push(0);
print minStack.push(-3);
print minStack.getMin();
print minStack.pop();
print minStack.top();
print minStack.getMin();

