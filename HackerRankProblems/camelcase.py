import sys

string = raw_input().strip()
count = 0
for i in string:
  if count == 0:
    count += 1
  else:
    if i.isupper():
      count += 1

print count

