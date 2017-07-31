'''
Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

Input Format

The first line contains the number of test cases T. T test cases follow:

    The first line of each test case contains a number N. The next line contains N integers, denoting the predicted price of WOT shares for the next N days.

    Constraints

    All share prices are between 1 and 100000
    Output Format

    Output T lines, containing the maximum profit which can be obtained for the corresponding test case.

    Sample Input

    3
    3
    5 3 2
    3
    1 2 100
    4
    1 3 1 2
    Sample Output

    0
    197
    3
    Explanation

    For the first case, you cannot obtain any profit because the share price never rises. 
    For the second case, you can buy one share on the first two days, and sell both of them on the third day. 
    For the third case, you can buy one share on day 1, sell one on day 2, buy one share on day 3, and sell one share on day 4.
'''


def max_profit(row):
    '''return max profit for given prices'''
    print "Starting to calculate"
    max_price = 0
    profit = 0
    for i in reversed(row):
        print "Now i is ",i
        if max_price < i:
            max_price = i
        profit += max_price - i
    print profit

if __name__ == "__main__":

    n = int(raw_input().strip())
    print "Number iterations is ", n
    for _ in xrange(n):
        length = int(raw_input().strip())
        row = map(int, raw_input().strip().split())
        max_profit(row)

