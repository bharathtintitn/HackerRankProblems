import sys




def split_array(array):
    '''
    Split array into two parts, and check sum of two parts.
    If equal return index of two array.
    Else return None.
    '''

    if len(array) > 1:
        total = sum(array)
    else:
        return None

    i = 0
    j = len(array) - 1
    right_sum = 0
    left_sum = 0
    print total
    half_total = total/2
    print half_total
    while i<=j:
        print "right_sum %d,left_sum %d, i %d j %d" % (right_sum,left_sum, i, j)
        if right_sum < half_total:
            right_sum += array[i]
            i += 1
        else:
            if right_sum != half_total:
                return None,0,0
            left_sum += array[j]
            j -= 1

    if right_sum == left_sum:
        return True, i, j
    return None,0,0


def count_split(array, length):
    '''
    '''



    count, i, j = split_array(array,length)

if __name__ == "__main__":

    N = int(raw_input().strip())
    for _ in xrange(N):
        length = int(raw_input().strip())
        array = map(int, raw_input().strip().split())
        print split_array(array)


