



def twoSum(nums, target):
	length = len(nums) - 1	
        nums = sorted(nums)
        print nums
	for i,j in enumerate(nums):
		search = target - j
		#print "search:", search
		mid = binary_search(nums, i+1, length, search)
		#print "mid:", mid
		if mid:
			return [i, mid]


def binary_search(arr, start, end, target):

	if start > end:
		return 0

	mid = (start + end)/2
	if arr[mid] == target:
		return mid
	elif arr[mid] < target:
		start = mid + 1
	else:
		end = mid - 1
	return binary_search(arr, start, end, target)

def find_index(nums, target):
    hashmap = {}
    for i,j in enumerate(nums):
        hashmap[j] = i

    for i,j in enumerate(nums):
        search = target - j
        if hashmap[search]:
            return [i, hashmap[search]]
        
#print twoSum([3,2,4], 6)
#print binary_search([3,2,4], 0, 2, 4)
print find_index([3,2,4],6)

