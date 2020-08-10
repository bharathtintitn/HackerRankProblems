class Solution(object):
    def findRestaurant(self, list1, list2):

		rest = {}
		if len(list1) < len(list2):
			go = list1
			no = list2
		else:
			go = list2
			no = list1

		for i,j in enumerate(go):
			rest[j] = i+1

		print "rest:", rest
		max_index = float('inf')
		mhotel = ''

		for i, res in enumerate(no):
			print "res:", res, " i:", i
			if rest.get(res, False):
				hotel = res
				index = rest[res] + i - 1
				if index < max_index:
					mhotel = res
					max_index = index
					print "current:", mhotel, " ", max_index

		print "Max:", max_index, " hotel:", mhotel
		return mhotel
		


a = Solution()
print a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
print a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
