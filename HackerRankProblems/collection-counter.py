import sys
from collections import Counter

N = raw_input().strip()
size = map(int, raw_input().strip().split())
#print size

size_counter = Counter(size)
#print size_counter

customers = int(raw_input().strip())
#print customers
total = 0
for _ in xrange(customers):

    cust = map(int, raw_input().strip().split())
    #print cust
    try:
        if size_counter[cust[0]] > 0:
            size_counter[cust[0]] -= 1
            total += cust[1]

    except:
        #print "size not available"

print total
