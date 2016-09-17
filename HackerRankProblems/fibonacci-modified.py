import sys

'''
We define a modified Fibonacci sequence using the following definition:
Given terms and where , term is computed using the following relation:
For example, if term t1 = 0 and  t2=1, term t3 = 0+1^2 = 1, term t4 = 1 + 1^2 = 2, term
t5 = 1 + 2^2 = 5, and so on.
Given three integers, t1, t2, and n, compute and print term tn of a modified Fibonacci sequence.

Input Format
A single line of three space-separated integers describing the respective values of t1, t2, and n.
Constraints
tn may exceed the range of a 64-bit integer.
Output Format
Print a single integer denoting the value of term tn in the modified Fibonacci sequence where the first two
terms are t1 and t2.
'''


def fibonacci(t1, t2, n):

  while n-2 > 0:
    t1, t2 = t2, t2*t2 + t1
    n -= 1
    #print "t1: {}, t2: {}, n: {}".format(t1,t2,n)
  return t2 

def main():

  assert fibonacci(0,1,5) == 5
  assert fibonacci(0,1,10) == 84266613096281243382112 

if __name__ == "__main__":

  main()
