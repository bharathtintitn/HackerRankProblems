import pdb
class Solution(object):

    def binary_search(self, letters, target, start, end):

        if start < end:
            mid = (end - start)/2 + start
            #print "mid: ", mid
            if letters[mid] == target:
                return self.binary_search(letters, target, mid+1, end)
            elif letters[mid] > target:
                return self.binary_search(letters, target, start, mid - 1)
            else:
                return self.binary_search(letters, target, mid+1, end)

        return start

    def nextGreat(self, letters, target):


        index = self.binary_search(letters, target, 0, len(letters)-1)
        print "index: ", index, "letter:", letters[index]
        if letters[index] == target:
            if index == len(letters)-1:
                return letters[0]
            return letters[index+1]
        elif letters[index] < target:
            if index == len(letters) - 1:
                return letters[0]
            return letters[index+1]
        return letters[index]
        #if index > 0 and index < len(letters) - 1:
        #    if target < letters[index]:
        #        return index
        #    elif target < letter[index - 1]:
        #        return index - 1
        #    else:
        #        return index + 1


a = Solution()
print a.nextGreat(["c", "f", "j"], 'a')
print a.nextGreat(["c", "f", "j"], 'c')
print a.nextGreat(["c", "f", "j"], 'd')
print a.nextGreat(["c", "f", "j"], 'g')
print a.nextGreat(["c", "f", "j"], 'j')
print a.nextGreat(["c", "f", "j"], 'k')
pdb.set_trace()
print a.nextGreat(["e","e","e","e","e","e","n","n","n","n"],'e')


