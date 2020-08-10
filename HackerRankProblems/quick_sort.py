


def quick_sort(a, start, end):

    if end > start:
        pivot = partition(a, start, end)
        quick_sort(a, start, pivot - 1)
        quick_sort(a, pivot + 1, end)

def partition(a, start, end):

    pivot = a[start]
    left = start + 1
    right = end

    while right >= left:
        if pivot > a[left]:
            left += 1
        elif pivot < a[right]:
            right -= 1
        else:
            a[left], a[right] = a[right], a[left]

    a[start] = a[right]
    a[right] = pivot
    print "A:", a
    return right


a =  [5, 4, 10, 11, 3, 2, 15]
 
a = [2, 3, 4, 5]

a = [10, 9, 8, 6]

a = []
a = [1]
quick_sort(a, 0, len(a)-1)
print "Final:", a
