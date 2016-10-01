def bubble_sort(a, n):
  swap = 0
  for i in xrange(n):
    for j in xrange(n - 1):
      #print "Before i: {} j:{} a[j+1]: {} a[j]: {} array:{}".format(i,j,a[j+1],a[j],a)
      if a[j] > a[j+1]:
        temp = a[j+1]
        a[j+1] = a[j]
        a[j] = temp
        swap += 1
        #print "After i: {} j:{} a[j+1]: {} a[j]: {} array:{}".format(i,j,a[j+1],a[j],a)
    if swap == 0:
        break
  #print a
  return swap, a[0], a[n-1]





if __name__ == "__main__":

  n = int(raw_input().strip())
  a = map(int, raw_input().strip().split())
  swap, a , b = bubble_sort(a,n)
  print "Array is sorted in {} swaps.".format(swap)
  print "First Element: {}".format(a)
  print "Last Element: {}".format(b)
