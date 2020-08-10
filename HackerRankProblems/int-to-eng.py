class Solution(object):
	def numberToWords(self, num):
                if num == 0:
                    return "Zero"

		billion = num//1000000000
		#print "billion:", billion
		million = (num - (billion*1000000000))//1000000
		#print "Million:", million
		thousand = (num - (million*1000000) - (billion*1000000000))//1000
                #print "thousand:", thousand
                rest = (num - (million*1000000) - (billion*1000000000) - (thousand*1000))
                #print "rest:", rest

                result = ''
                if billion:
                    if self.string_one(billion):
                        result += self.string_one(billion) + ' Billion '
                    else:
                        ret = self.threes(billion)
                        result += ret + ' Billion'
                if million:
                    if self.string_one(million):
                        result += self.string_one(million) + ' Million '
                    else:
                        ret = self.threes(million)
                        result += ret + ' Million '
                if thousand:
                    if self.string_one(thousand):
                        result += self.string_one(thousand) + ' Thousand '
                    else:
                        ret = self.threes(thousand)
                        result += ret + ' Thousand '
                if rest:
                    if self.string_one(rest):
                        result += self.string_one(rest)
                    else:
                        ret = self.threes(rest)
                        result += ret

                print result.strip()
                self.remove_space(result)
                return result.strip()

        def remove_space(self, string):
            result = ''
            result = " ".join(string.split())
            print "Result: ", result

        def threes(self, num):
            ones = num//100
            #print "Threes ones:", ones
            twos = (num - (ones*100))
            #print "Threes twos:", twos
            rest = (num - (ones*100) - twos)
            #print "rest:", rest
            result = ''
            if ones:
                if self.string_one(ones):
                    result += self.string_one(ones) + ' Hundred '
            if twos:
                if self.string_20(twos):
                    result += self.string_20(twos) + ' '
                else:
                    result += self.twos(twos)
            if rest:
                if self.string_one(rest):
                    result += self.string_one(rest)

            return result

        def twos(self, num):

            ones = num//10
            #print "Twos ones:", ones
            rest = (num - (ones*10))
            #print "Twos rest:", rest
            result = ''
            if ones:
                if ones:
                    result += self.string_10s(ones) + ' '
            if rest:
                if rest:
                    result += self.string_one(rest)

            return result

	def string_one(self, num):

		if num ==  1: return "One";
		if num ==  2: return "Two";
		if num ==  3: return "Three";
		if num ==  4: return "Four";
		if num ==  5: return "Five";
		if num ==  6: return "Six";
		if num ==  7: return "Seven";
		if num ==  8: return "Eight";
		if num ==  9: return "Nine";

	def string_20(self, num):

		if num ==  10: return "Ten";
		if num ==  11: return "Eleven";
		if num ==  12: return "Twelve";
		if num ==  13: return "Thirteen";
		if num ==  14: return "Fourteen";
		if num ==  15: return "Fifteen";
		if num ==  16: return "Sixteen";
		if num ==  17: return "Seventeen";
		if num ==  18: return "Eighteen";
		if num ==  19: return "Nineteen";

	def string_10s(self, num):

		if num ==  2: return "Twenty";
		if num ==  3: return "Thirty";
		if num ==  4: return "Forty";
		if num ==  5: return "Fifty";
		if num ==  6: return "Sixty";
		if num ==  7: return "Seventy";
		if num ==  8: return "Eighty";
		if num ==  9: return "Ninety";

a = Solution()
a.numberToWords(1234567891)
a.numberToWords(1234567)
a.numberToWords(123)
a.numberToWords(12)
a.numberToWords(2)
a.numberToWords(50868)
a.numberToWords(12345)

