import sys

n = int(raw_input().strip())
string = raw_input().strip()

print string
print n

level = 0
prevarilevel = 0 
varilevel = 0
valley = 0

for i in string:
  if i == 'U':
    prevarilevel = varilevel 
    varilevel += 1
  elif i == 'D':
    prevarilevel = varilevel 
    varilevel -= 1

  print varilevel, prevarilevel, valley, i
  if varilevel == 0:
    if not prevarilevel:
      valley += 1

print valley


