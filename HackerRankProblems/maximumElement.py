import sys

N = raw_input().strip()
N = int(N)

print "N:",N
stack = []
for i in xrange(N):
	row = map(int, raw_input().strip().split())
	print row
	x = row[0]
	print x
	if x == 1:
		stack.push(row[1])
	elif x == 2:
		print stack.pop()
	elif x == 3:
		print max(stack)

