import sys
from collections import defaultdict


def buttons(row, n, p):

    row.sort()
    freq = defaultdict(lambda: None)
    total = 0
    for i in row:
        q, r = divmod(i, p)
        #print "money {}, cost {}, quo {}, remainder {}".format(i, p, q, r)
        if r > 0:
            q += 1

        #print "freq is ", freq
        while freq[q]:
            q += 1
        #print "q is ", q
        freq[q] = True
        total = total + q
        #print "total is ", total

    return total


if __name__ == "__main__":

    row = map(int, raw_input().strip().split())
    n, p = row[0], row[1]
    row = map(int, raw_input().strip().split())
    #print row
    print buttons(row, n, p)
