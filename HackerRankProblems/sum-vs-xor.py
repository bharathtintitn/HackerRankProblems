import sys

n = long(raw_input().strip())

count = 0
for i in xrange(n+1):
    if n+i  == n^i:
        count += 1

print count



print 2**(bin(n)[2:].count('0')) if n else 1

