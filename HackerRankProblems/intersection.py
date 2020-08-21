'''
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
'''


def merge(intervals_a, intervals_b):
	result = []

	len_a = len(intervals_a)
	len_b = len(intervals_b)
	result = []
	i, j = 0, 0
	while i < len_a and j < len_b:
		start = max(intervals_a[i][0], intervals_b[j][0])
		end = min(intervals_a[i][1], intervals_b[j][1])
		# if overlap
		if start <= end:
			# if there is a overlap add to result list
			if intervals_a[i][0] <= start <= intervals_a[i][1] and \
				intervals_b[j][0] <= start <= intervals_b[j][1] and \
				intervals_b[j][0] <= end <= intervals_b[j][1] and \
				intervals_a[i][0] <= end <= intervals_a[i][1]:
					result.append([start, end])
					if intervals_a[i][1] <= end:
						i += 1
					if intervals_b[j][1] <= end:
						j += 1
		else:
			if intervals_a[i][1] <= end:
				i += 1
			if intervals_b[j][1] <= end:
				j += 1
	print('result:{}'.format(result))
	return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
