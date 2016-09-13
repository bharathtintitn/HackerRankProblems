import sys

t = int(raw_input().strip())
open_braces = ['[','{','(']
close_braces = [']','}',')']
braces = {']': '[', '}': '{', ')':'('}
done = False
for a0 in xrange(t):
  s = raw_input().strip()
  done = False
  stack = []
  for i in s:
    if i not in braces:
      stack.append(i)
    else:
      if not stack:
        print "NO"
        done = True
        break;
      brac = stack.pop()
      #print 'brac is ',brac," ",braces[i]
      if brac != braces[i]:
        print "NO"
        done = True
        break;
  if not done:
    if stack:
        print "NO"
    else:
        print "YES"
