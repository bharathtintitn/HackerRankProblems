import sys

'''
Alice has a binary string, , of length . She thinks a binary string is beautiful if and only if it doesn't contain the substring.

In one step, Alice can change a  to a  (or vice-versa). Count and print the minimum number of steps needed to make Alice see the
 string as beautiful.

Input Format

The first line contains an integer,  (the length of binary string ). 
The second line contains a single binary string, , of length .

Constraints

Each character in .
Output Format

Print the minimum number of steps needed to make the string beautiful.
'''


def beautiful_binary_string(string):

  string_to_find = '010'
  index = 0
  length = len(string)
  count = 0

  while index < length and length > 2:
    #print "string is ", string[index:index+3], "index+3 = ",index+3
    if length >= index+3 and string[index:index+3] == string_to_find:
      count += 1
      index += 3
    else:
      index += 1

  #print count
  return count
    
    


def main():

  assert beautiful_binary_string("0101010") == 2
  assert beautiful_binary_string("01100") == 0
  assert beautiful_binary_string("0100101010") == 3
  

if __name__ == "__main__":

  main()
