import sys

N = int(raw_input().strip())
stack = []
max_element = -9999 
max_item = []
count = -1 
for _ in xrange(N):
  row = map(int, raw_input().strip().split())
  if row[0] == 1:
    stack.append(row[1])
    if count == -1 or max_item[count] <= row[1]:
      max_item.append(row[1])
      count += 1
  elif row[0] == 2:
    item = stack.pop()
    if item == max_item[count]:
      max_item.pop(count)
      count -= 1
  else:
    print max_item[count] 

