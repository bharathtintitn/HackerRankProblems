import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a, n):
	sorted_a = sorted(a)
	import pdb
	pdb.set_trace()
	print sorted_a
	max_count = 0
	for index in xrange(n-1):
	    i = index + 1
	    count = 0
	    element = sorted_a[index]
	    while i < n:
		    diff = sorted_a[i] - element
		    if diff <= 1:
			    count += 1
		    else:
				break
		    if max_count < count:
			    max_count = count
		    i += 1
	return max_count + 1
if __name__ == '__main__':

    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a, n)
    print result
