'''
Louise and Richard play a game. They have a counter set to . Louise gets the first turn and the turns alternate thereafter. In the game, they perform the following operations.

If  is not a power of , reduce the counter by the largest power of  less than .
If  is a power of , reduce the counter by half of .
The resultant value is the new  which is again used for subsequent operations.
The game ends when the counter reduces to 1, i.e., , and the last person to make a valid move wins.

Given , your task is to find the winner of the game.

Update If they set counter to , Richard wins, because its Louise' turn and she cannot make a move.

Input Format 
The first line contains an integer , the number of testcases. 
 lines follow. Each line contains , the initial number set in the counter.

Constraints

Note: Range of  is larger than long long int, consider using unsigned long long int.

Output Format

For each test case, print the winner's name in a new line. So if Louise wins the game, print "Louise". Otherwise, print "Richard". (Quotes are for clarity)

Sample Input

1
6
Sample Output

Richard
Explanation

As  is not a power of , Louise reduces the largest power of  less than  i.e., , and hence the counter reduces to .
As  is a power of , Richard reduces the counter by half of  i.e., . Hence the counter reduces to .
As we reach the terminating condition with , Richard wins the game.
'''

def winner(value):

  binary = bin(value)
  binary = binary[2:]
  start_one_count = False
  one_count = 0
  zero_count = 0
  for i in reversed(binary):
    if i == '1' and not start_one_count:
      start_one_count = True
      continue
    
    if start_one_count and i == '1':
      one_count += 1
    elif i == '0' and not start_one_count:
      zero_count += 1

  total = zero_count + one_count
  print "zero_count {} one_count {} and total {}".format(zero_count, one_count, total)
  if total%2 == 0:
    print "Richard"
  else:
    print "Louise"

if __name__ == "__main__":

  N = int(raw_input().strip())
  for _ in xrange(N):
    value = int(raw_input().strip())
    winner(value)
