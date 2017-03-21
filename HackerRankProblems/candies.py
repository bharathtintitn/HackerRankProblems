import sys


def count(rank, N):
    total = 0
    prev = None
    for i in xrange(N):
        if i == 0:
            total = total + 1
            prev = 1
        else:
            if rank[i] > rank[i-1]:
                total = total + prev + 1
                prev = prev + 1
            elif rank[i] <= rank[i-1]:
                total = total + 1
                prev = 1
        print prev,total

    print total
    rtotal = 0
    rprev = None
    for i in reversed(xrange(N)):
        if i == N-1:
            rtotal = rtotal + 1
            rprev = 1
        else:
            if rank[i] > rank[i-1]:
                rtotal = rtotal + rprev + 1
                rprev = rprev + 1
            elif rank[i] <= rank[i-1]:
                rtotal = rtotal + 1
                rprev = 1
        print rprev,rtotal
    print rtotal

    return rtotal if rtotal < total else total

N = int(raw_input().strip())

ranking = []
for _ in xrange(N):
    ranking.append(int(raw_input().strip()))

#print ranking

print count(ranking, N)
