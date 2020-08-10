import copy
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_dict = {}
        for i in p:
            if p_dict.get(i, False):
                p_dict[i] = p_dict[i] + 1 
            else:
                p_dict[i] = 1
            
        print "p-dict", p_dict
        
        temp = copy.deepcopy(p_dict)
        
        end = 0
        begin = 0
        length = len(temp)
        count = length
	import pdb
	pdb.set_trace()
        while end < len(s):
            item = s[end]
            if temp.get(item, False):
                temp[item] = temp[item] - 1
                if temp[item] == 0:
                    del temp[item]
                    count -= 1
                        
                if count == 0:
                    result.append(begin)
                    temp = copy.deepcopy(p_dict)
		    count = length 
                    begin = end
                    continue
                end += 1
                
            else:
                if length <> count:
                    count = length
                    temp = copy.deepcopy(p_dict)
		
		if not temp.get(item, False):
		   end += 1
		begin = end	
	    if end > 4:
			#pdb.set_trace()
                        pass
                    
        return result
                    
            
               

a = Solution()
print a.findAnagrams("abacbabc", "abc")
