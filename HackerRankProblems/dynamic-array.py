import sys
import pdb

firstRow = map(int, raw_input().strip().split(' '))
N = firstRow[0]
testcases = firstRow[1]

lastAns = 0
seqList = []
for i in xrange(N):
	seqList.append([])

for i in xrange(testcases):
	#print "enter row"
	row = map(int, raw_input().strip().split(' '))
	n, x, y = row[0], row[1], row[2]
	z = (x^lastAns)%N
	#pdb.set_trace()
	if n == 1:
		#print "in case 1 ", z, N, seqList, y
		if(z<N):
			seqList[z].append(y)
		#print seqList
	elif n == 2:
		w = y%(len(seqList[z]));
		#print "w is ", w, z, seqList, y
		lastAns = seqList[z][w]
		#print seqList[z]
		print lastAns

