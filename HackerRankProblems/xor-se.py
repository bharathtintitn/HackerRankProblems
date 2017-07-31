'''
An array, , is defined as follows:

     for , where  is the symbol for XOR
     You must answer  questions. Each  question, is in the form , and the answer is  (the Xor-Sum of segment ).

     Print the answer to each question.

     Input Format

     The first line contains  (the number of questions).
     The  subsequent lines each contain two space separated integers,  and , respectively. Line contains  and .

     Constraints 



     Subtasks 
     For  score: 

         Output Format

         On a new line for each test case , print the exclusive-or of 's elements in the inclusive range between indices and .

         Sample Input

         3
         2 4
         2 8
         5 9
         Sample Output

         7
         9
         15
'''

import sys






X = lambda i: [i, 2, i+2, 0][(i%8)//2]
for _ in xrange(input()):
        L, R = map(long, raw_input().strip().split())
        print X(R) ^ X(L-1)
