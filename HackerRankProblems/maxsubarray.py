import sys

def max_subarray(length, array):


    temp = [-9999]*length
    total = None
    for i,element in enumerate(array):
        if not total:
            temp[i] = element
            total = element
        else:
            if total < total+element and total > 0:
               total = total + element
            else:
                total = element
            temp[i] = total
        print temp, total

    print temp
    print max(temp)




T = int(raw_input().strip())
print "No of test cases is ", T

for _ in xrange(T):
    N = int(raw_input().strip())
    row = map(int, raw_input().strip().split())
    print "NO of element %d and list is %s" % (N, row)
    max_subarray(N, row)

