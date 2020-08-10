import pdb
from collections import defaultdict
class Solution(object):
    def reorderLogFiles(self, logs):
		string = defaultdict(list)
		nums = []
		for log in logs:
			index = log.find(' ')
			key = log[index+1:]
			value = log[:index]
			#string[key] = value
			if key[0].isdigit():
				nums.append(log)
			else:
				string[key].append(value)
		print string
		pdb.set_trace()
		keys = string.keys()
		keys = sorted(keys)
		print keys
		print nums
		result = []
		for log in keys:
			val = string[log]
			val = sorted(val)
			for v in val:
				result.append(v + ' ' + log)
		result.extend(nums)
		print result


a = Solution()
a.reorderLogFiles(["a1 9 2 3 1","g1 act car",
			"zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])

print "*****"

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"] 
l = filter(lambda l: l[l.find(' ')+1].isalpha(), logs)
print 'l:',l
d = filter( lambda d: d[d.find(' ')+1].isdigit(), logs)
print d
