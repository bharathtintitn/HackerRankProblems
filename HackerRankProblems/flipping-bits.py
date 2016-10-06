'''
You will be given a list of 32 bits unsigned integers. You are required to output the list of
the unsigned integers you get by flipping bits in its binary representation (i.e. unset 
bits must be set, and set bits must be unset).

Input: 1 (bin: 00000000000000000000000000000001)
ouput: 4294967294  (bin: 11111111111111111111111111111110)
'''





def flip_number(n):

  flip_number = ""
  binary = bin(n)
  binary = binary[2:]

  unsigned_number = binary.zfill(32)

  #print unsigned_number

  for i in unsigned_number:
    if i == '0':
      flip_number += '1'
    else:
      flip_number += '0'

  #print flip_number
  return int(flip_number,2)



N = int(raw_input().strip())

for _ in xrange(N):

  number = int(raw_input().strip())
  print flip_number(number)
