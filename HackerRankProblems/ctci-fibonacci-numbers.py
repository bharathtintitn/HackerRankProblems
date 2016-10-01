
def fibonacci(n):
    # Write your code here.
    # print n

    memo = [0]*(n+1)
    return fib(n, memo)

def fib(n, memo):

    if n <= 0:
        return 0
    if n == 1:
        return 1
  
    if memo[n] != 0:
      return memo[n]

    memo[n-1] = fib(n-1, memo) 
    memo[n-2] = fib(n-2, memo)

    return memo[n-1] + memo[n-2]

n = int(raw_input())
print(fibonacci(n))
