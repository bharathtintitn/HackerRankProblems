



def get_number(number, arr,start,  n):

	end = n - 1
	while start <=  end:
		mid = (start + end)/2
		#print "mid:", mid
		if arr[mid] == number:
			return number
		elif arr[mid] > number:
			end = mid - 1
		elif arr[mid] < number:
			start = mid + 1
	return None

def pairs(n, k, arr):

	arr.sort()
	pairs = {}
        count = 0
	#print "arr:", arr
        import pdb
        #pdb.set_trace()
	for i in xrange(n-1):
		first_number = arr[i]
		search_number = first_number + k
		#print search_number
		second_number = get_number(search_number, arr,i+1, n)
                #print "a: ", first_number, " b: ", second_number
		if second_number:
			count += 1
        #print count
        return count


if __name__ == "__main__":

    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = map(int, raw_input().rstrip().split())
    result = pairs(n, k, arr)
    print result
