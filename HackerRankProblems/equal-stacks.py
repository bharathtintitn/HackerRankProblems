'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

    The second line contains  space-separated integers describing the cylinder heights in stack .
    The third line contains  space-separated integers describing the cylinder heights in stack .
    The fourth line contains  space-separated integers describing the cylinder heights in stack .
    Constraints

    Output Format

    Print a single integer denoting the maximum height at which all stacks will be of equal height.

    Sample Input

    5 3 4
    3 2 1 1 1
    4 3 2
    1 1 4 1
    Sample Output

    5
'''






from __future__ import print_function

import os
import sys
import pdb

from itertools import accumulate
from collections import Counter

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1c, h2c, h3c = [list(accumulate(reversed(l))) for l in (h1, h2, h3)]
print(h1c)
print(h2c)
print(h3c)
total_stack = h1c + h2c + h3c
print(total_stack)
counter_stack = Counter(total_stack)
print(counter_stack)
print(counter_stack.items())
try:
    print(max(i[0] for i in counter_stack.items() if i[1] == 3))
except:
    print(0)
