'''
Mark and Jane are very happy after having their first kid. Their son is very fond of toys, so Mark wants to buy some. There are  different toys lying in front of him, tagged with their prices, but he has only . He wants to maximize the number of toys he buys with this money.

Now, you are Mark's best friend and have to help him buy as many toys as possible.

Input Format

The first line contains two integers,  and , followed by a line containing  space separated integers indicating the products' prices.

Constraints

 
  
   
   A toy can't be bought multiple times.

   Output Format

   An integer that denotes maximum number of toys Mark can buy for his son.

   Sample Input

   7 50
   1 12 5 111 200 1000 10
   Sample Output

   4
   Explanation

   He can buy only 4 toys at most. These toys have the following prices: 1,12,5,10.

'''



import sys

def maximumToys(prices, k, n):
    # Complete this function

	array = sorted(prices)
	print array
	total = 0
	i = -1
	while total < k and i < n:
		#print i, total, array[i]
		i += 1
		total += array[i]
		if total > k:
			total -= array[i]
			break
	return i

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k, n)
    print result
