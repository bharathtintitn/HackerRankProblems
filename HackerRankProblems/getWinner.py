import pdb

class Solution(object):

    def getWinner(self, arr, k):
        print "**********"
        i, j = 0, 1
        i_count, j_count = 0, 0
        a,b = arr[i], arr[j]

        while i < len(arr) and j < len(arr):
            #pdb.set_trace()
            if arr[i] < arr[j]:
                b = arr[j]
                i = j+1 if j > i else i+1
                i_win = True
                i_count += 1
                j_win = False
                j_count = 0
            else:
                a = arr[i]
                j = i+1 if i > j else j+1
                i_win = False
                i_count = 0
                j_win = True
                j_count += 1

            #print "a:{}, b:{}, arr[i]:{}, arr[j]:{}, i:{}, j:{}, j_c:{}, i_c:{}".format(a, b, arr[i], arr[j], i, j, j_count, i_count)
            if j_count >= k:
                return a
            if i_count >=k:
                return b



        if a > b:
            return a
        return b

a = Solution()
print a.getWinner([2,1,3,5,4,6,7], 2)
print a.getWinner([3,2,1], 10)
print a.getWinner([1,9,8,2,3,7,6,4,5], 7)
print a.getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000)

