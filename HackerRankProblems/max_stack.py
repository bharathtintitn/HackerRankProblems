class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.tops = -1
        self.max_array = []
        self.max_number = float('-inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.tops += 1
        self.array.append(x)
        if self.max_number < x:
            self.max_number = x
        self.max_array.append(self.max_number)

    def pop(self):
        """
        :rtype: int
        """
        if self.tops == -1:
            return None
        x = self.array.pop()
        max_num = self.max_array.pop()
        self.tops -= 1
        if self.tops > -1:
            self.max_number = self.max_array[self.tops]
        else:
            self.max_number = float('-inf')
        return x

    def top(self):
        """
        :rtype: int
        """
        
        if self.tops == -1:
            return None
        x = self.array[self.tops]
        return x

    def peekMax(self):
        """
        :rtype: int
        """
        print "PeekMax:", self.tops, ' ', self.max_array
        if self.tops == -1:
            return None
        x = self.max_array[self.tops]
        print "peekmax return:", x
        return x
    
    def popMax(self):
        """
        :rtype: int
        """
        if self.tops == -1:
            return None
        ret = self.max_number
        index = self.tops
        next_max = None
        while index > -1:
	    print 'Index:', index, ' ret:', ret, " ", self.max_array
            if self.max_array[index] == ret:
                if ret == self.array[index]:
                    break
                else:
                    if not next_max:
                        next_max = self.array[index]
                        
                    if next_max < self.array[index]:
                        next_max = self.array[index]
                index -= 1
                
        if index > -1:
            self.max_array.pop()
            self.array.pop(index)
            self.tops -= 1
       
        print "popmax:", next_max, "index:", index, " top:", self.tops, "array:", self.array
        if next_max:
            if self.tops > -1:
                if self.max_array[self.tops] <> ret and next_max < self.max_array[self.tops]:
                    next_max = self.max_array[self.tops]
                    
                while index <= self.tops:
                    self.max_array[index] = next_max
                    index += 1
             
        if self.tops == -1:
            self.max_number = float('-inf')
        else:
            self.max_number = self.max_array[self.tops]
                    
        print "MaxArray:", self.max_array
        return ret

stack = MaxStack()
stack.push(5); 
stack.push(1);
stack.push(-5);
print stack.array
print stack.top();
import pdb
pdb.set_trace()
print stack.popMax()
print stack.popMax()
print stack.top();
