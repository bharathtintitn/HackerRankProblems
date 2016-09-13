import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
a = ""
arr = reversed(arr)
#print arr
for i in arr:
	a = a + str(i) + ' '
#print len(a)
print a
#a = a.strip()
#print a[::-1]

