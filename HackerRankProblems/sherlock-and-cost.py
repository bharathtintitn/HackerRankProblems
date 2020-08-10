#!/bin/python

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    total = 0
    row_max = 0
    for i in xrange(len(B) - 1):
        row_max = 0
        for j in xrange(1, B[i]+1):
            for k in xrange(1, B[i+1] + 1):
                if abs(j-k) > row_max:
                    row_max = abs(j-k)
        print("total:{}".format(total))
        print('row_max:{}'.format(row_max))
        total += row_max
    return total
    
if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        B = map(int, raw_input().rstrip().split())

        result = cost(B)


