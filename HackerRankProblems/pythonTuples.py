import sys
n = raw_input()
a = map(int, raw_input().strip().split())
print a
print hash(tuple(a))
