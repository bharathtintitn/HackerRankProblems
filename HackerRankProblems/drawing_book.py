import sys


n = int(raw_input().strip())
p = int(raw_input().strip())

left = p/2
right = (n/2) - (p/2)

print left," ",right

print left if left > right else right

