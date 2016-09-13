import sys

firstrow = map(int,raw_input().strip().split())
n = firstrow[0]
d = firstrow[1]

secondrow = map(str,raw_input().strip().split())
length = len(secondrow)
result = ' '
if d > length:
  d = d%length
test = result.join(secondrow[d:length])

for i in xrange(d):
  test = test + ' ' + secondrow[i]
print test
