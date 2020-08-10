import pdb

def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  i, j, total, length = 0, 0, 0, 0
  min_length = float('inf')
  print(s)
  print(arr)
  #pdb.set_trace()
  while j < len(arr):
    #pdb.set_trace()
    total += arr[j]
    j += 1
    while total >= s and i <= j:
        length = j - i 
        print('inside: i:{}, j:{}, length:{}, total:{}'.format(i, j, length, total))
        min_length = min(length, min_length)
        total -= arr[i]
        i += 1
    print("i:{}, j:{}, length:{}, total:{}".format(i, j, length, total))

  return -1 if min_length == float('inf') else min_length

print smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])
print smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])
print smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])
