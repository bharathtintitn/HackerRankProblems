import pdb


def remove_element1(arr, key):

  index = 0
  i = index

  while index < len(arr) and i < len(arr):
    #pdb.set_trace()
    print("index:{}".format(index))
    while arr[index] != key:
      index += 1

    i = index + 1
    print("index:{}, i:{}".format(index, i))
    while arr[i] == key:
      i += 1
      print("i:",i)
    if i < len(arr):
	print("arr[index]:{}, arr[i]:{}, index:{}, i:{}, arr:{}".format(arr[index], arr[i], index, i, arr))
	arr[index], arr[i] = arr[i], arr[index]
	if arr[index] != key:
	  index = index + 1
    else:
	break

  print(arr)

def remove_element(arr, key):

	n = 0
	for i in range(len(arr)):
		if arr[i] != key:
			arr[n], arr[i] = arr[i], arr[n]
			n += 1

	print(arr)




def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()

