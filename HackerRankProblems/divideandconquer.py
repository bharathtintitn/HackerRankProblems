
class Solution(object):

    def searchMatrix(self, matrix, target):

        def binary_search(array, start, end, find):

            if start <= end:
                mid = (start+end)/2
                print 'mid:', mid
                if array[mid] == find:
                    return True
                elif array[mid] < find:
                    return binary_search(array, mid+1, end, find)
                else:
                    return binary_search(array, start, mid-1, find)
            return False

        length = len(matrix)
        if length > 0:
            breath = len(matrix[0])
        else:
            return False

        def go_find(matrix, target, index):
            if index > length-1:
                return False
            array = matrix[index]
            if binary_search(array, 0, breath-1, target):
                return True
            return go_find(matrix, target, index+1)

        return go_find(matrix, target, 0)


a = Solution()
print a.searchMatrix([[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]], 5)
print a.searchMatrix([[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]], 20)

