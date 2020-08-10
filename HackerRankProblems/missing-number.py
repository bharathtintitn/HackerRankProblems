'''
Numeros the Artist had two lists that were permutations of one another. He was very proud. Unfortunately, while transporting them from one exhibition to another, some numbers were lost out of the first list. Can you find the missing numbers?

Notes

If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
The difference between maximum and minimum number in the second list is less than or equal to .
Input Format

There will be four lines of input:

     - the size of the first list,  
     The next line contains  space-separated integers  
      - the size of the second list,  
      The next line contains  space-separated integers 

      Constraints

      Output Format

      Output the missing numbers in ascending order.

      Sample Input

      10
      203 204 205 206 207 208 203 204 205 206
      13
      203 204 204 205 206 207 205 208 203 206 205 206 204
      Sample Output

      204 205 206
      Explanation

       is present in both arrays. Its frequency in  is , while its frequency in  is . Similarly,  and  occur twice in , but three times in . The rest of the numbers have the same frequencies in both lists.
'''


import pdb

def missingNumbers(arr,brr,m,n):

    pdb.set_trace()
    indexi = 0
    indexj = 0
    arr.sort()
    brr.sort()
    print arr
    print brr
    missing = m - n
    missingSet = set()
    while indexi < n or indexj < m  or len(missingSet) < missing:
        item = arr[indexi]
        if item != brr[indexj]:
            missingSet.add(brr[indexj])
            indexj += 1
        indexj += 1
        indexi += 1
    print missingSet
    print " ".join(map(str, missingSet))

if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    m = int(raw_input())
    brr = map(int, raw_input().rstrip().split())
    result = missingNumbers(arr, brr, m, n)


