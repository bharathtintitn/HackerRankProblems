class Solution(object):
	def divison(self, n):

		if n == 0:
			return 0
		if n == 1:
			return 1

		if n%2 == 0:
			return self.divison(n/2)

		return self.divison((n/2) + 1)

	def get_number(self, n, result):

		if result > n:
			return result/2
		return self.get_number(n, result*2)

	def rec(self, number, record):
		print "Number:", number
		if number > 16:
			res = self.get_number(number, 1)
			temp = number - res
			print "Res:", res
			print "temp:", temp
			return self.rec(temp, record+1)
		return number, record

	def kthGrammar(self, k):
			string = '0110100110010110'
			if k > 16:
				num, record = self.rec(k, 0)
				print "ret:", num, " record:", record
				get = string[num-1]
				print "get:", get
				if record%2 == 0:
					return get
				else:
					if get == '0':
						return '1'
					return '0'
			else:
				return string[k-1]
a = Solution()
#a.kthGrammar(10 ,4)
print a.divison(1)
print a.divison(0)
print a.divison(4)
print a.divison(10)
print 'find number'

#print a.get_number(434991989, 1)
#print a.rec(417219134)
print a.kthGrammar(417219134)
