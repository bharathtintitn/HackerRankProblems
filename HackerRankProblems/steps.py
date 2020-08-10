

def getSteps(n):

    if n == 0:
        return 1
    if n == -1:
        return 0

    return getSteps(n-1) + getSteps(n-2)


def newSteps(n):

    dp = [None]*(n+1)
    dp[0] = 1
    dp[1] = 1
    print "dp:", dp
    for i in xrange(2,n+1):
        #print i, dp[0], dp[1], i-1, i-2
        dp[i] = dp[i-1] + dp[i-2]
    print "f", dp
    return dp[-1]


print getSteps(6)
print newSteps(6)
