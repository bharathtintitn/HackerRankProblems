

def is_matched(expression):

  bdict = { '{': '}', '[': ']', '(': ')' }
  length = len(expression)
  if length % 2 != 0 or length == 0:
    return False

  bindex = length / 2
  aindex = bindex - 1 
  while bindex < length and aindex >= 0:
    print "a:{} b:{} mid:{} start:{}".format( \
      expression[aindex], expression[bindex],bindex,aindex)
    if bdict[expression[aindex]] != expression[bindex]: 
      return False
    bindex += 1
    aindex -= 1

  return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
