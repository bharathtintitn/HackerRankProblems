import sys

N = raw_input().strip()
N = int(N)
#print N
strings = []
for i in xrange(N):
  strings.append(raw_input().strip())

#print strings

Q = raw_input().strip()
Q = int(Q)
#print Q
query = []
for i in xrange(Q):
  query.append(raw_input().strip())

#print query

for i in query:
 count = 0
 for j in strings:
   if i == j:
     count += 1 
 print count
