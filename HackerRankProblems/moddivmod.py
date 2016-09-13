from __future__ import division
import sys

a = raw_input().strip()
a = int(a)

b = raw_input().strip()
b = int(b)

print a//b
print a%b
print divmod(a,b)
