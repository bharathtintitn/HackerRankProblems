

def fib(n):

    n0 = 0
    n1 = 1
    f = [n0, n1]
    for i in xrange(2, n):
        f.append(f[i-1]+f[i-2])
    print f
    return f[n-1]

def recfib(n):

    if n > 10:
        return n

    return n + recfib(n+1)
temp = [None]*11
def recfibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if temp[n]:
        return temp[n]

    res = recfibo(n-1) + recfibo(n-2)
    temp[n] = res
    return res

print "temp:", temp
print recfibo(9)
print "after:", temp


print fib(10)
print recfib(0)
