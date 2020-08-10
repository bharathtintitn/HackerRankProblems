

class Solution:

    def __init__(self, nums):

        self.data = [0 for _ in nums] + nums
        print self.data

        self.n = len(nums)

        for i in reversed(range(1, self.n)):
            print "i:", i , " ", self.data[i], " 2*i:", 2*i, " ", self.data[2*i], " 2*i+1:", 2*i+1, " ", self.data[2*i+1]
            self.data[i] = self.data[2*i] + self.data[2*i+1]

        print "after:", self.data


    def update(self, index, val):
        i = index + self.n
        self.data[i] = val
        while i >= 1:
            i //= 2
            self.data[i] = self.data[2*i] + self.data[2*i+1]

    def sumRange(self, i, j):
        left = self.n + i
        right = self.n + j 
        sumrange = 0
        import pdb
        pdb.set_trace()
        while left < right:
             print "Left:", left, " Right:", right
             if left%2:
                    sumrange += self.data[left]
                    left += 1
             if right%2:
                  sumrange += self.data[right]
                  right -= 1
             left //= 2
             right //= 2
        return sumrange

    def sum2(self, i, j):

        left = self.n + i
        right = self.n + j
        import pdb
        pdb.set
        sumrange = 0
        while True:
            
            print "left:", left, " ", self.data[left], " Right:", right, "  ", self.data[right]
            if left%2:
                parent = left//2
                print "in left, parent: ", parent, " ", self.data[parent]
                sumrange += self.data[parent]
                


#a = Solution([1, 3, 5])
a = Solution([1, 3, 5, 4, 10])
a = Solution([1, 3, 5, 4, 10, 20])
a = Solution([30, 1, 3, 5, 4, 10, 20])
print a.sumRange(1,4)
