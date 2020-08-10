
def display(dp):

    for i in xrange(len(dp)):
        print " ".join(map(str, dp[i]))

def longestCommonSubsequence(text1, text2):

    len_a = len(text1)
    len_b = len(text2)

    print len_a, len_b

    dp = [[None for i in xrange(len_a+1)] for j in xrange(len_b+1)]

    #print "dp:", dp
    display(dp)

    for i in xrange(len_b+1):
        for j in xrange(len_a+1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                #dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        #display(dp)

    print "Final:"
    print display(dp)


longestCommonSubsequence("abcde", "ace")
longestCommonSubsequence("abc", "abc")
longestCommonSubsequence("abc", "def")
longestCommonSubsequence("bsbininm", "jmjkbkjkv")
