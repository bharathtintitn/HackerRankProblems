import sys
import math


def sum_of_digits(divisor):

    sum_list = [sum(map(int, str(number))) for number in divisor]
    return sum_list

n = int(raw_input().strip())
divisor = []
for i in xrange(1,int(math.sqrt(n))+2):
    if n%i == 0:
        if n/i == i:
            divisor.append(i)
        else:
            divisor.append(i)
            divisor.append(n/i)

#print divisor
result = sum_of_digits(divisor)
mini = -999999
index = None
for i,j in enumerate(result):

    #print i,j, result[i], divisor[i]
    if j > mini:
        mini = j
        index = i
    elif j == mini and divisor[i] < divisor[index]:
        mini = j
        index = i
    #print index,mini
#print "result ",result
#print "divisor ",divisor
print divisor[index]



