import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

#max_height = max(height)
#print max_height
#
#func = lambda x: x < max_height
#
#count = 0
#for i in height:
#  if i < max_height:
#    count += 1
#
#print count


height.sort()
print height
length = len(height)
print length
i = length
count =0 
max_height = height[length-1]

while i > 0:
  if height[i-1] == max_height:
    print count,i
    count += 1
    i -= 1
  else:
    break

print count



