import sys

'''
  Finding Maximizing XOR.
  Input: 10, 15
  Output: 7

  Eg:
  10^10 = 0
  10^11 = 1
  10^12 = 6
  10^13 = 7
  10^14 = 4
  10^15 = 5
  11^11 = 0
  .
  .
  .
  15^15 = 0

  max is 7.
'''

def  maxXor(l, r):
  values = []
  m = 0
  for i in xrange(l,r+1):
    for j in xrange(l,r+1):
      if i^j > m:
        m = i^j
        values.append((i,j,m))
    
  return m


def main():

  maxXor(10, 15) == 7
  maxXor(1, 10) == 15 
  maxXor(5, 6) == 3 

if __name__ == "__main__":

  main()
