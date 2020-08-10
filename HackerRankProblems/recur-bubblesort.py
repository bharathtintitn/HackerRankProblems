
def bubble_sort(a, i, j,  n):

    if i < n - 1:
        if j < n - 1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            bubble_sort(a, i+1, j, n)
            bubble_sort(a, i, j+1, n)

a = [1, 5, 4, 2, 8]
a = [8, 2, 4, 5, 1]
bubble_sort(a, 0, 0, len(a))
print a
