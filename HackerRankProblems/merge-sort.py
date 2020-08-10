import pdb


def m_sort(a, t, start, end):

    if start < end:

        mid = (end + start)/2
        print "mid = ", mid

        m_sort(a,t, start, mid)
        m_sort(a, t, mid + 1, end)
        m_merge(a, t, start, mid + 1, end)


def m_merge(a, t, start, mid, end):

    left = start
    right = mid
    index = start

    while left < mid and right <= end:
        if a[left]  > a[right]:
            t[index] = a[right]
            right += 1
            index += 1
        else:
            t[index] = a[left]
            left += 1
            index += 1

    while left < mid:
        t[index] = a[left]
        left += 1
        index += 1

    while right <= end:
        t[index] = a[right]
        right += 1
        index += 1

    print "t:",t
    print "A:",a
    for i in xrange(start, end+1):
        a[i] = t[i]


if __name__ == '__main__':

    a = [3, 2, 5, 6, 1, 0, 4]
    t = [None] * (len(a))
    pdb.set_trace()
    m_sort(a, t, 0, len(a) - 1)
    print a
    print t
