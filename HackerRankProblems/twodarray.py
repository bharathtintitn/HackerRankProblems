import sys

arr = []
for arr_i in xrange(6):
	    arr_temp = map(int,raw_input().strip().split(' '))
	    arr.append(arr_temp)

result = []
high = 0
for i in xrange(4):
	temp = []
	for j in xrange(4):
		total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
		temp.append(total)
		if high == 0:
			high = total
		if total > high:
			high = total

	result.append(temp)
print high

