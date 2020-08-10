class Solution(object):
    def spiralOrder(self, matrix):
		i_start = 0
		i_end = len(matrix)-1
		result = []
		if len(matrix) == 0:
			return result

		j_start = 0
		j_end = len(matrix[0])-1
		flip = True
		length = len(matrix)
		print "#######################"
		while (length%2 == 0 and i_start < i_end and j_end >= j_start) or (length%2 <> 0 and i_start <= i_end and j_end >= j_start):
			print "Length:", length, " istart:", i_start, " i_end:", i_end
			if flip:
				index = j_start
				while index <= j_end:
					result.append(matrix[i_start][index])
					index += 1
				i_start += 1

				inside = False
				index = i_start
				print "Flip:", flip, " index:", index, " j:", j_end, " result:", result
				while index <= i_end:
					result.append(matrix[index][j_end])
					index += 1
					inside = True
				#if inside:
				j_end -= 1

				index = j_end
				while index >= j_start and i_start <= i_end:
					result.append(matrix[i_end][index])
					index -= 1
				i_end -= 1
				flip = False
			else:
				index = j_start
				while index <= j_end:
					result.append(matrix[i_end][index])
					index += 1
				i_end -= 1

				index = i_end
				inside = False
				while index >= i_start:
					result.append(matrix[index][j_end])
					index -= 1
					inside = True
				j_end -= 1

				index = j_end
				while index >= j_start and i_start <= i_end:
					result.append(matrix[i_start][index])
					index -= 1
				i_start += 1
				flip = True
		print "Final istart:", i_start, " i_end:", i_end
		print "Result:", result
		return result

a = Solution()
a.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8],[9,10,11,12]])
a.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
				
