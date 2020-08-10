
class QuickSort(object):

    def quick_sort(self, array):
        pass
        length = len(array)
        if length <= 1:
            return array
        pivot = self.split_array(array)
        left = self.quick_sort(array[:pivot])
        right = self.quick_sort(array[pivot+1:])
        return left + [array[pivot]] + right


    def split_array(self, array):
        pivot = array[0]
        print "pivot:", pivot
        i = 1
        j = len(array)-1
        index = 0
        while i < j:
            while i < j:
                if array[i] <= pivot:
                    i += 1
                else:
                    break

            while i < j:
                if array[j] > pivot:
                    j -= 1
                else:
                    break

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

        if i == j:
            if array[i] < pivot:
                array[0], array[i] = array[i], pivot
                index = i
            else:
                array[i-1], array[0] = pivot, array[i-1]
                index = i - 1
        print "Pivot sorted array:", array, " index:", index
        return index


    def sort(self, array1, array2):
        pass

    def merge(self, array1, array2):
        pass

a = QuickSort()
print a.quick_sort([4, 1,3, 2, 7, 5, 6])
