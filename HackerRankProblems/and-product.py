import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    res = 0
    for k in range(32, -1, -1):
        s = 1<<k
	print '1: {}&{}::{}'.format(b,s,b&s)
        if b&s:
	    print '2: {}&{}::{}'.format(a,s,a&s)
            if a&s:
	        print '3: {}&{}::{}'.format(res,s,res|s)
                res |= s
            else:
                break
    return res

if __name__ == '__main__':

    n = int(raw_input())

    for n_itr in xrange(n):
        ab = raw_input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)
	print result



