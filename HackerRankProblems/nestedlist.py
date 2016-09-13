import sys

N = int(raw_input().strip())
twodlist = []
for i in xrange(N):
  temp = []
  temp.append(raw_input().strip())
  temp.append(float(raw_input().strip()))
  twodlist.append(temp)

arr = sorted(twodlist, key=lambda x:x[1])
print arr
num = arr[0][1]
nextnum = None
for i in xrange(1,N):
  print arr[i][1], num, nextnum
  if arr[i][1] > num and nextnum == None:
    print "result is ",arr[i][0]
    nextnum = arr[i][1]
  elif nextnum == arr[i][1]:
    print "result is ",arr[i][0]


