#!/bin/python

import math
import os
import random
import re
import sys
import pdb

# Complete the lilysHomework function below.
def lilysHomework(arr):

    length = len(arr)
    count = 0
    for i in xrange(length-1):
        element = arr[i]
        swap_element = None
        swap = False
	pdb.set_trace()
        for j in xrange(i+1, length):
            if arr[j] < element:
                if not swap_element or swap_element > arr[j]:
                    index = j
                    swap = True
                    swap_element = arr[j]

        if swap:
            arr[index], arr[i] = arr[i], arr[index]
            count += 1
	print "Count:", count
	print "i,",i
	print "arr:", arr
    print arr
    return count

if __name__ == '__main__':

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = lilysHomework(arr)



