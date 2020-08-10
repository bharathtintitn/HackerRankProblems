
def recur(left, right, number, result):

    if left >= 1:
        recur(left-1, right, number, result + '{')

    if right >= 1 and left < right:
        recur(left, right-1, number, result + '}')

    if len(result) == number*2:
        print result

def parent(number):

    recur(number, number, number, '')

import pdb
pdb.set_trace()
print parent(6)
