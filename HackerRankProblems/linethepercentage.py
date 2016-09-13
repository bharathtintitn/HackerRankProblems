from __future__ import division
import sys

N = int(raw_input().strip())
print N
records = {}
for _ in xrange(N):
  row = raw_input().strip().split()
  print row
  def a(x):
    try:
      float(x);
      return True
    except ValueError: 
      return False 
  records[row[0]] = [float(x) for x in row if a(x)]

print "records", records
name = raw_input().strip()
print name
print format(sum(records[name]) / 3, '.2f')
