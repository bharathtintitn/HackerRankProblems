class Solution(object):
    def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		lengtha = len(a)
		lengthb = len(b)
		indexa, indexb = lengtha-1, lengthb-1
		result = ''
		carry = '0'
		while indexa >= 0 or indexb >=0:
			chara, charb = '0','0'
			if indexa >= 0:
				chara = a[indexa]
				#chara = int(chara)
				indexa -= 1
			if indexb >= 0:
				charb = b[indexb]
				#charb = int(charb)
				indexb -= 1
			if chara == '0' and charb == '0':
				if carry == '1':
					res = '1'
					carry = '0'
				else:
					res = '0'
					carry = '0'
			elif (chara == '0' and charb == '1') or (chara == '1' and charb == '0'):
				if carry == '1':
					res = '0'
					carry = '1'
				else:
					res = '1'
					carry = '0'
			else:
				if carry == '1':
					res = '1'
					carry = '1'
				else:
					res = '0'
					carry = '1'
			result = res + result
		if carry == '1':
			result = carry + result
		print "result:", result
		return result

a = Solution()
print a.addBinary("11", '1')
print a.addBinary("1010", '1011')

			
			
				
