import pdb
class Solution(object):
    def numMatchingSubseq(self, S, words):
		print "***************"
		dick = {}
		for word in words:
			if dick.get(word, False):
				dick[word][3] += 1
			else:
				length = len(word) - 1
				dick[word] = [False, 0, length, 1]

		print "Dick:", dick
		count = 0
		for i in S:
			#pdb.set_trace()
			print "i:", i, " dick:", dick
			for key, value in dick.iteritems():
				if not value[0]:
					index = value[1]
					length = value[2]
					if i == key[index]:
						if index == length:
							value[0] = True
							count += value[3]
							del dick[key]
						else:
							value[1] += 1
		print "count:", count
		return count

a = Solution()
print a.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
print a.numMatchingSubseq("qlhxagxdqh",["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"])
