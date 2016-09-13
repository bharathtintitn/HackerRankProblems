import sys


def insertionSort(array):
  '''
  Implementation of Insertion sort.
  '''

  for i in reversed(xrange(len(array))):
    value = array[i]
    index = None
    #print 'i is ',i, ' value is ',value
    j = i - 1
    while j >= 0:
      #print 'j is ',j
      if value < array[j]:
        array[j+1] = array[j]
        index = j
        print " ".join(map(str,array))
      j -= 1
      
    if index:
      array[index] = value
      print array

size = int(raw_input().strip())
array = map(int, raw_input().strip().split())

print size, array

insertionSort(array)
