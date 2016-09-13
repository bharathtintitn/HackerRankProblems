test_cases = raw_input()
print test_cases
test_cases = int(test_cases)

def find_pattern(p_mat, l_mat, p_row, p_col, l_row, l_col):
	pattern_str = p_mat[0][0]
	print pattern_str 
	for j in xrange(l_row):
		if pattern_str in l_mat[j][0]:
			for i in range(p_row):
				begin = 0
				start_index = l_row[j][0].index(pattern_str, begin)
				for row in xrange(p_col-1):
					if p_mat[row+1][0] in l_mat[j+row][0]:
						next_start_index = l_mat[j+row].index(p_mat[row+1][0], begin)
					else:
						break
			print "Yes"


for i in range(test_cases):
	l_row, l_col = raw_input().split(' ')
	l_col = int(l_col)
	l_row = int(l_row)
	print l_row, l_col
	l_mat = []
	for j in range(l_row):
		l_mat.append(raw_input().split(' '))

	print l_mat
	p_row, p_col = raw_input().split(' ')
	p_row = int(p_row)
	p_col = int(p_col)
	print p_row, p_col
	p_mat = []
	for k in range(p_row):
		p_mat.append(raw_input().split(' '))

	print p_mat
	find_pattern(p_mat, l_mat, p_row, p_col)	
