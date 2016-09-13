import sys

L = []
N = raw_input().strip()
N = int(N)

for _ in xrange(N):
	s = raw_input().strip().split()
	cmd = s[0]
	arg = s[1:]
	
	if cmd != "print":
		cmd += "("+",".join(arg)+")"
		eval("L."+cmd)
	else:
		print L
