import sys

N = int(raw_input().strip())
arr = map(int, raw_input().strip().split())
a = arr.sort()

length = len(arr)
m = arr[length-1]
for i in reversed(xrange(length-1)):
  if arr[i] != m:
    print arr[i]
    break

